#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;


// from my toolbox
vector<string> tokenize(string str, const string delimiter = " ")
{
    vector<string> ret;
    size_t pos = 0;
    while ((pos = str.find(delimiter)) != std::string::npos) {
        string token = str.substr(0, pos);
        if (!token.empty()) {
            ret.push_back(token);
        }
        str.erase(0, pos + delimiter.length());
    }
    if (!str.empty()) {
        ret.push_back(str);
    }
    return ret;
}


void read_intcode(const std::string& filename, int*& program, size_t& length)
{
    fstream fs;
    fs.open(filename, fstream::in);
    std::string prog_str;
    fs >> prog_str;
    fs.close();

    vector<string> prog_tokens = tokenize(prog_str, ",");
    length = prog_tokens.size();
    program = new int[length];
    for (size_t i = 0; i < length; ++i) {
        program[i] = atoi(prog_tokens[i].c_str());
    }
}


constexpr size_t MAX_OPERANDS = 3;  // maximum operands an instruction can have

void decode_instruction(const int instruction,
                        int& opcode,
                        int* addr_mode)  // addr_mode[MAX_OPERANDS]
{
    opcode = instruction % 100;
    for (size_t i = 0, op = instruction / 100; i < MAX_OPERANDS;
         ++i, op /= 10) {
        addr_mode[i] = op % 10;
    }
}


void decode_operands(const int* const program,
                     size_t& pc,
                     const size_t opd_count,
                     const int* addr_mode,
                     int* operands)
{
    assert(opd_count <= MAX_OPERANDS);
    for (int i = 0; i < opd_count; ++i) {
        const int raw = program[pc++];
        operands[i] = addr_mode[i] == 0 ? program[raw] : raw;
    }
}


void debug_instr(const int instruction,
                 const size_t opd_count,
                 const int* const addr_mode,
                 const int* const operands)
{
    cerr << "instr " << instruction << " = " << (instruction % 100) << "/";
    assert(opd_count <= MAX_OPERANDS);
    for (int i = 0; i < opd_count; ++i) {
        if (i > 0) {
            cerr << ".";
        }
        cerr << addr_mode[i];
    }
    cerr << " (";
    for (int i = 0; i < opd_count; ++i) {
        if (i > 0) {
            cerr << ",";
        }
        cerr << operands[i];
    }
    cerr << ") ";
}


// if inputs is null, then inputs are read from cin; otherwise they are *all*
// read from inputs[], which must contain enough entries
int run_intcode(int* program,
                const size_t length,
                const int* const inputs = nullptr,
                const bool debug = false)
{
    // if (debug) {
    //    for (size_t pc = 0; pc < length; ++pc) {
    //        cerr << "[" << pc << "] = " << program[pc] << "\n";
    //    }
    //}

    int input_ix = 0;
    int last_output = -1;

    size_t pc = 0;
    while (pc < length && program[pc] != 99) {
        if (debug) {
            cerr << "PC=" << pc << " >>> ";
        }
        const int instruction = program[pc++];
        int opcode;
        int addr_mode[MAX_OPERANDS];
        int opd[MAX_OPERANDS];
        decode_instruction(instruction, opcode, addr_mode);
        switch (opcode) {
            case 1:                // add
                addr_mode[2] = 1;  // destination address
                decode_operands(program, pc, 3, addr_mode, opd);
                assert(opd[2] < length);
                program[opd[2]] = opd[0] + opd[1];
                if (debug) {
                    debug_instr(instruction, 3, addr_mode, opd);
                    cerr << " ::: [" << opd[2] << "] := " << program[opd[2]]
                         << "\n";
                }
                break;
            case 2: {
                addr_mode[2] = 1;  // destination address
                decode_operands(program, pc, 3, addr_mode, opd);
                assert(opd[2] < length);
                program[opd[2]] = opd[0] * opd[1];
                if (debug) {
                    debug_instr(instruction, 3, addr_mode, opd);
                    cerr << " ::: [" << opd[2] << "] := " << program[opd[2]]
                         << "\n";
                }
                break;
            }
            case 3: {              // input
                addr_mode[0] = 1;  // destination address
                decode_operands(program, pc, 1, addr_mode, opd);
                assert(opd[0] < length);
                if (inputs == nullptr) {
                    cout << "Input? ";
                    std::string str;
                    cin >> str;
                    program[opd[0]] = stoi(str);
                } else {
                    program[opd[0]] = inputs[input_ix++];
                }
                if (debug) {
                    debug_instr(instruction, 1, addr_mode, opd);
                    cerr << " ::: [" << opd[0] << "] := " << program[opd[0]]
                         << "\n";
                }
                break;
            }
            case 4: {  // output
                decode_operands(program, pc, 1, addr_mode, opd);
                if (debug) {
                    debug_instr(instruction, 1, addr_mode, opd);
                    cerr << " ::: ";
                }
                last_output = opd[0];
                cout << "Output: " << opd[0] << "\n";
                break;
            }
            case 5: {  // jump-if-true
                decode_operands(program, pc, 2, addr_mode, opd);
                if (opd[0] != 0) {
                    pc = opd[1];
                }
                if (debug) {
                    debug_instr(instruction, 2, addr_mode, opd);
                    cerr << " ::: PC := " << pc << "\n";
                }
                break;
            }
            case 6: {  // jump-if-false
                decode_operands(program, pc, 2, addr_mode, opd);
                if (opd[0] == 0) {
                    pc = opd[1];
                }
                if (debug) {
                    debug_instr(instruction, 2, addr_mode, opd);
                    cerr << " ::: PC := " << pc << "\n";
                }
                break;
            }
            case 7: {              // less than
                addr_mode[2] = 1;  // destination address
                decode_operands(program, pc, 3, addr_mode, opd);
                assert(opd[2] < length);
                program[opd[2]] = opd[0] < opd[1] ? 1 : 0;
                if (debug) {
                    debug_instr(instruction, 3, addr_mode, opd);
                    cerr << " ::: [" << opd[2] << "] := " << program[opd[2]]
                         << "\n";
                }
                break;
            }
            case 8: {              // equals
                addr_mode[2] = 1;  // destination address
                decode_operands(program, pc, 3, addr_mode, opd);
                assert(opd[2] < length);
                program[opd[2]] = opd[0] == opd[1] ? 1 : 0;
                if (debug) {
                    debug_instr(instruction, 3, addr_mode, opd);
                    cerr << " ::: [" << opd[2] << "] := " << program[opd[2]]
                         << "\n";
                }
                break;
            }
            default: {
                cerr << "bad instruction: " << instruction << "\n";
                exit(-1);
            }
        }
    }

    return last_output;
}


int main(const int argc, const char* argv[])
{
    constexpr bool DEBUG = false;

    int* orig_program;
    size_t length;
    read_intcode(argv[1], orig_program, length);

    int* program[5];
    for (int p = 0; p <= 4; ++p) {
        program[p] = new int[length];
    }

    int inputs[2];
    int high = 0;
    int phase[5] = {0, 1, 2, 3, 4};
    do {
        // make 5 copies of original program
        for (int p = 0; p <= 4; ++p) {
            for (size_t i = 0; i < length; ++i) {
                program[p][i] = orig_program[i];
            }
        }

        cout << phase[0] << " " << phase[1] << " " << phase[2] << " "
             << phase[3] << " " << phase[4] << ":\n";
        inputs[0] = phase[0];
        inputs[1] = 0;

        inputs[1] = run_intcode(program[0], length, inputs);
        inputs[0] = phase[1];

        inputs[1] = run_intcode(program[1], length, inputs);
        inputs[0] = phase[2];

        inputs[1] = run_intcode(program[2], length, inputs);
        inputs[0] = phase[3];

        inputs[1] = run_intcode(program[3], length, inputs);
        inputs[0] = phase[4];

        const int out = run_intcode(program[4], length, inputs);
        if (out > high) {
            high = out;
        }
    } while (next_permutation(phase, phase + 5));

    cout << "\nhigh = " << high << "\n";

    exit(0);
}
