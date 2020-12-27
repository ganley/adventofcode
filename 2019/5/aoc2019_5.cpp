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

void decode_instruction(const size_t instruction,
                        size_t& opcode,
                        size_t addr_mode[MAX_OPERANDS])
{
    opcode = instruction % 100;
    for (size_t i = 0, op = instruction / 100; i < MAX_OPERANDS; ++i, op /= 10) {
        addr_mode[i] = op % 10;
    }
}


void run_intcode(int* program, const size_t length, const bool debug = false)
{
    if (debug) {
        for (size_t pc = 0; pc < length; ++pc) {
            cerr << "[" << pc << "] = " << program[pc] << "\n";
        }
    }

    size_t pc = 0;
    while (pc < length && program[pc] != 99) {
        const size_t instruction = program[pc++];
        size_t opcode;
        size_t addr_mode[MAX_OPERANDS];
        decode_instruction(instruction, opcode, addr_mode);
        switch (opcode) {
            case 1:         // add (1) and multiply (2)
            case 2: {
                const size_t src0 = program[pc++];
                const int opd0 = addr_mode[0] == 0 ? program[src0] : src0;
                const size_t src1 = program[pc++];
                const int opd1 = addr_mode[1] == 0 ? program[src1] : src1;
                assert(addr_mode[2] == 0);  // destination always immediate
                const size_t dst = program[pc++];
                program[dst] = opcode == 1 ? opd0 + opd1 : opd0 * opd1;
                if (debug) {
                    cerr << "instr " << instruction << " = " << opcode
                         << "/" << addr_mode[0] << "." << addr_mode[1] << "."
                         << addr_mode[2] << " ==> " << "src0=" << src0
                         << " opd0=" << opd0 << " src1=" << src1
                         << " opd1=" << opd1 << ": [" << dst << "] := "
                         << program[dst] << "\n";
                }
                break;
            }
            case 3: {       // input
                const size_t dst = program[pc++];
                assert(addr_mode[0] == 0);  // destination always immediate
                cout << "Input? ";
                std::string str;
                cin >> str;
                program[dst] = stoi(str);
                if (debug) {
                    cerr << "input: " << dst << " := " << program[dst] << "\n";
                }
                break;
            }
            case 4: {       // output
                const size_t src = program[pc++];
                const int opd0 = addr_mode[0] == 0 ? program[src] : src;
                if (debug) {
                    cerr << "output: src=" << src << "\n";
                }
                cout << "Output [" << src << "]/" << addr_mode[0] << ": "
                     << opd0 << "\n";
                break;
            }
            default: {
                cerr << "bad instruction: " << program[pc] << "\n";
                exit(-1);
            }
        }
    }
}


int main(const int argc, const char* argv[])
{
    constexpr bool DEBUG = false;

    int* program;
    size_t length;
    read_intcode(argv[1], program, length);

    int* backup = new int[length];
    for (size_t i = 0; i < length; ++i) {
        backup[i] = program[i];
    }

    // part 1
    run_intcode(program, length, DEBUG);

    if (DEBUG) {
        for (size_t pc = 0; pc < length; ++pc) {
            cerr << "[" << pc << "] = " << program[pc] << "\n";
        }
    }

    exit(0);
}

