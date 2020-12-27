#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;


// from my toolbox
static vector<string> tokenize(string str, const string delimiter = " ");


class Program {
public:
    // if inputs is null, then inputs are read from cin; otherwise they are
    // *all* read from inputs[], which must contain enough entries
    int run(const int* const inputs = nullptr,
            const bool debug = false)
    {
        // if (debug) {
        //    for (size_t pc = 0; pc < length; ++pc) {
        //        cerr << "[" << pc << "] = " << m_memory[pc] << "\n";
        //    }
        //}

        int input_ix = 0;
        int last_output = -1;

        while (m_pc < m_length) {
            if (debug) {
                cerr << "PC=" << m_pc << " >>> ";
            }
            const int instruction = m_memory[m_pc++];
            int opcode;
            int addr_mode[MAX_OPERANDS];
            int opd[MAX_OPERANDS];
            decode_instruction(instruction, opcode, addr_mode);
            switch (opcode) {
                case 1:                // add
                    addr_mode[2] = 1;  // destination address
                    decode_operands(3, addr_mode, opd);
                    assert(opd[2] < m_length);
                    m_memory[opd[2]] = opd[0] + opd[1];
                    if (debug) {
                        debug_instr(instruction, 3, addr_mode, opd);
                        cerr << " ::: [" << opd[2] << "] := " << m_memory[opd[2]]
                            << "\n";
                    }
                    break;
                case 2: {
                    addr_mode[2] = 1;  // destination address
                    decode_operands(3, addr_mode, opd);
                    assert(opd[2] < m_length);
                    m_memory[opd[2]] = opd[0] * opd[1];
                    if (debug) {
                        debug_instr(instruction, 3, addr_mode, opd);
                        cerr << " ::: [" << opd[2] << "] := " << m_memory[opd[2]]
                            << "\n";
                    }
                    break;
                }
                case 3: {              // input
                    addr_mode[0] = 1;  // destination address
                    decode_operands(1, addr_mode, opd);
                    assert(opd[0] < m_length);
                    if (inputs == nullptr) {
                        cout << "Input? ";
                        std::string str;
                        cin >> str;
                        m_memory[opd[0]] = stoi(str);
                    } else {
                        m_memory[opd[0]] = inputs[input_ix++];
                    }
                    if (debug) {
                        debug_instr(instruction, 1, addr_mode, opd);
                        cerr << " ::: [" << opd[0] << "] := " << m_memory[opd[0]]
                            << "\n";
                    }
                    break;
                }
                case 4: {  // output
                    decode_operands(1, addr_mode, opd);
                    if (debug) {
                        debug_instr(instruction, 1, addr_mode, opd);
                        cerr << " ::: ";
                    }
                    last_output = opd[0];
                    cout << "Output: " << opd[0] << "\n";
                    break;
                }
                case 5: {  // jump-if-true
                    decode_operands(2, addr_mode, opd);
                    if (opd[0] != 0) {
                        m_pc = opd[1];
                    }
                    if (debug) {
                        debug_instr(instruction, 2, addr_mode, opd);
                        cerr << " ::: PC := " << m_pc << "\n";
                    }
                    break;
                }
                case 6: {  // jump-if-false
                    decode_operands(2, addr_mode, opd);
                    if (opd[0] == 0) {
                        m_pc = opd[1];
                    }
                    if (debug) {
                        debug_instr(instruction, 2, addr_mode, opd);
                        cerr << " ::: PC := " << m_pc << "\n";
                    }
                    break;
                }
                case 7: {              // less than
                    addr_mode[2] = 1;  // destination address
                    decode_operands(3, addr_mode, opd);
                    assert(opd[2] < m_length);
                    m_memory[opd[2]] = opd[0] < opd[1] ? 1 : 0;
                    if (debug) {
                        debug_instr(instruction, 3, addr_mode, opd);
                        cerr << " ::: [" << opd[2] << "] := " << m_memory[opd[2]]
                            << "\n";
                    }
                    break;
                }
                case 8: {              // equals
                    addr_mode[2] = 1;  // destination address
                    decode_operands(3, addr_mode, opd);
                    assert(opd[2] < m_length);
                    m_memory[opd[2]] = opd[0] == opd[1] ? 1 : 0;
                    if (debug) {
                        debug_instr(instruction, 3, addr_mode, opd);
                        cerr << " ::: [" << opd[2] << "] := " << m_memory[opd[2]]
                            << "\n";
                    }
                    break;
                }
                case 99: {              // halt
                    if (debug) {
                        cerr << "halt\n";
                    }
                    return last_output;
                }
                default: {
                    cerr << "bad instruction: " << instruction << "\n";
                    exit(-1);
                }
            }
        }
    
        return last_output;
    }

    void read(const std::string& filename)
    {
        fstream fs;
        fs.open(filename, fstream::in);
        std::string prog_str;
        fs >> prog_str;
        fs.close();

        vector<string> prog_tokens = tokenize(prog_str, ",");
        m_length = prog_tokens.size();
        m_memory = new int[m_length];
        for (size_t i = 0; i < m_length; ++i) {
            m_memory[i] = atoi(prog_tokens[i].c_str());
        }
    }

    Program()
    :   m_pc(0),
        m_length(0),
        m_memory(nullptr)
    {
    }

    Program(const Program& rhs)
    :   m_pc(rhs.m_pc),
        m_length(rhs.m_length)
    {
        m_memory = new int[m_length];
        for (int i = 0; i < m_length; ++i) {
            m_memory[i] = rhs.m_memory[i];
        }
    }

    const Program& operator=(const Program& rhs)
    {
        m_pc = rhs.m_pc;
        m_length = rhs.m_length;
        m_memory = new int[m_length];
        for (int i = 0; i < m_length; ++i) {
            m_memory[i] = rhs.m_memory[i];
        }
        return *this;
    }

    ~Program()
    {
        delete[] m_memory;
    }

private:
    static void decode_instruction(const int instruction,
                                   int& opcode,
                                   int* addr_mode)  // addr_mode[MAX_OPERANDS]
    {
        opcode = instruction % 100;
        for (size_t i = 0, op = instruction / 100;
             i < MAX_OPERANDS;
             ++i, op /= 10) {
            addr_mode[i] = op % 10;
        }
    }

    void decode_operands(const size_t opd_count,
                         const int* addr_mode,
                         int* operands)
    {
        assert(opd_count <= MAX_OPERANDS);
        for (int i = 0; i < opd_count; ++i) {
            const int raw = m_memory[m_pc++];
            operands[i] = addr_mode[i] == 0 ? m_memory[raw] : raw;
        }
    }

    static void debug_instr(const int instruction,
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

private:
    size_t m_pc = 0;
    size_t m_length = 0;
    int* m_memory = nullptr;

    static constexpr size_t MAX_OPERANDS = 3;
};


int main(const int argc, const char* argv[])
{
    constexpr bool DEBUG = false;

    Program orig;
    orig.read(argv[1]);

    Program program[5];

    int inputs[2];
    int high = 0;
    int phase[5] = {0, 1, 2, 3, 4};
    do {
        // make 5 copies of original program
        for (int p = 0; p <= 4; ++p) {
            program[p] = orig;
        }

        cout << phase[0] << " " << phase[1] << " " << phase[2] << " "
             << phase[3] << " " << phase[4] << ":\n";
        inputs[0] = phase[0];
        inputs[1] = 0;

        inputs[1] = program[0].run(inputs);
        inputs[0] = phase[1];

        inputs[1] = program[1].run(inputs);
        inputs[0] = phase[2];

        inputs[1] = program[2].run(inputs);
        inputs[0] = phase[3];

        inputs[1] = program[3].run(inputs);
        inputs[0] = phase[4];

        const int out = program[4].run(inputs);
        if (out > high) {
            high = out;
        }
    } while (next_permutation(phase, phase + 5));

    cout << "\nhigh = " << high << "\n";

    exit(0);
}


// from my toolbox
vector<string> tokenize(string str, const string delimiter)
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

