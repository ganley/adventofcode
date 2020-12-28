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
    typedef enum { INIT, RUN, WAIT, HALT } state_t;
    typedef long long int mem_t;

    mem_t run(const mem_t* const inputs,
              const size_t num_inputs,
              const bool debug = false)
    {
        m_state = RUN;

        size_t input_ix = 0;

        while (m_pc < m_size) {
            if (debug) {
                cerr << "PC=" << m_pc << " >>> ";
            }
            const mem_t instruction = m_memory[m_pc++];
            mem_t opcode;
            mem_t addr_mode[MAX_OPERANDS];
            mem_t* opd[MAX_OPERANDS];
            decode_instruction(instruction, opcode, addr_mode);
            switch (opcode) {
                case 1:                // add
                    decode_operands(3, addr_mode, opd);
                    *(opd[2]) = *(opd[0]) + *(opd[1]);
                    if (debug) {
                        debug_instr(instruction, 3, addr_mode, opd);
                        cerr << " ::: [" << (opd[2] - m_memory) << "] := "
                             << *(opd[2]) << "\n";
                    }
                    break;
                case 2: {
                    decode_operands(3, addr_mode, opd);
                    *(opd[2]) = *(opd[0]) * *(opd[1]);
                    if (debug) {
                        debug_instr(instruction, 3, addr_mode, opd);
                        cerr << " ::: [" << (opd[2] - m_memory) << "] := "
                             << *(opd[2]) << "\n";
                    }
                    break;
                }
                case 3: {              // input
                    decode_operands(1, addr_mode, opd);
                    if (input_ix >= num_inputs) {
                        m_state = WAIT;
                        m_pc -= 2;     // rewind to start of input instruction
                        return 0;
                    }
                    *(opd[0]) = inputs[input_ix++];
                    if (debug) {
                        debug_instr(instruction, 1, addr_mode, opd);
                        cerr << " ::: [" << (opd[0] - m_memory) << "] := "
                             << *(opd[0]) << "\n";
                    }
                    break;
                }
                case 4: {  // output
                    decode_operands(1, addr_mode, opd);
                    if (debug) {
                        debug_instr(instruction, 1, addr_mode, opd);
                        cerr << " ::: " << *(opd[0]) << "\n";
                    }
                    return *(opd[0]);
                }
                case 5: {  // jump-if-true
                    decode_operands(2, addr_mode, opd);
                    if (*(opd[0]) != 0) {
                        m_pc = *(opd[1]);
                    }
                    if (debug) {
                        debug_instr(instruction, 2, addr_mode, opd);
                        cerr << " ::: PC := " << m_pc << "\n";
                    }
                    break;
                }
                case 6: {  // jump-if-false
                    decode_operands(2, addr_mode, opd);
                    if (*(opd[0]) == 0) {
                        m_pc = *(opd[1]);
                    }
                    if (debug) {
                        debug_instr(instruction, 2, addr_mode, opd);
                        cerr << " ::: PC := " << m_pc << "\n";
                    }
                    break;
                }
                case 7: {              // less than
                    decode_operands(3, addr_mode, opd);
                    *(opd[2]) = *(opd[0]) < *(opd[1]) ? 1 : 0;
                    if (debug) {
                        debug_instr(instruction, 3, addr_mode, opd);
                        cerr << " ::: [" << (opd[2] - m_memory) << "] := "
                             << *(opd[2]) << "\n";
                    }
                    break;
                }
                case 8: {              // equals
                    decode_operands(3, addr_mode, opd);
                    *(opd[2]) = *(opd[0]) == *(opd[1]) ? 1 : 0;
                    if (debug) {
                        debug_instr(instruction, 3, addr_mode, opd);
                        cerr << " ::: [" << (opd[2] - m_memory) << "] := "
                             << *(opd[2]) << "\n";
                    }
                    break;
                }
                case 9: {               // adjust relative base
                    decode_operands(1, addr_mode, opd);
                    m_relbase += *(opd[0]);
                    if (debug) {
                        debug_instr(instruction, 1, addr_mode, opd);
                        cerr << " ::: relbase += " << *(opd[0])
                             << " now " << m_relbase << "\n";
                    }
                    break;
                }
                case 99: {              // halt
                    if (debug) {
                        cerr << "halt\n";
                    }
                    m_state = HALT;
                    return 0;
                }
                default: {
                    cerr << "bad instruction: " << instruction << "\n";
                    exit(-1);
                }
            }
        }

        assert(false);
    }

    void run_interactive(const bool debug = false)
    {
        mem_t inputs[1];
        size_t num_inputs = 0;
        while (m_state != HALT) {
            const auto out = run(inputs, num_inputs, debug);
            switch (m_state) {
            case RUN:
                cout << "Output: " << out << "\n";
                num_inputs = 0;
                break;
            case WAIT:
                cout << "Input? ";
                cin >> inputs[0];
                num_inputs = 1;
                break;
            default:
                break;
            }
        }
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
        m_size = m_length + EXTRA_MEM;
        m_memory = new mem_t[m_size];
        for (size_t i = 0; i < m_length; ++i) {
            m_memory[i] = atoll(prog_tokens[i].c_str());
        }
        for (size_t i = m_length; i < m_size; ++i) {
            m_memory[i] = 0;
        }

        reset();
    }

    void reset()
    {
        m_pc = 0;
        m_relbase = 0;
        m_state = INIT;
    }

    state_t state()
    {
        return m_state;
    }

    Program()
    :   m_pc(0),
        m_relbase(0),
        m_length(0),
        m_size(0),
        m_memory(nullptr),
        m_state(INIT)
    {
    }

    Program(const Program& rhs)
    :   m_pc(rhs.m_pc),
        m_relbase(rhs.m_relbase),
        m_length(rhs.m_length),
        m_size(rhs.m_size),
        m_state(rhs.m_state)
    {
        m_memory = new mem_t[m_size];
        for (size_t i = 0; i < m_size; ++i) {
            m_memory[i] = rhs.m_memory[i];
        }
    }

    const Program& operator=(const Program& rhs)
    {
        m_pc = rhs.m_pc;
        m_relbase = rhs.m_relbase;
        m_length = rhs.m_length;
        m_size = rhs.m_size;
        m_memory = new mem_t[m_size];
        for (size_t i = 0; i < m_size; ++i) {
            m_memory[i] = rhs.m_memory[i];
        }
        m_state = rhs.m_state;
        return *this;
    }

    ~Program()
    {
        delete[] m_memory;
    }

private:
    static void decode_instruction(const mem_t instruction,
                                   mem_t& opcode,
                                   mem_t* addr_mode)  // addr_mode[MAX_OPERANDS]
    {
        opcode = instruction % 100;
        for (size_t i = 0, op = instruction / 100;
             i < MAX_OPERANDS;
             ++i, op /= 10) {
            addr_mode[i] = op % 10;
            assert((addr_mode[i] >= 0) && (addr_mode[i] <= 2));
        }
    }

    void decode_operands(const size_t opd_count,
                         const mem_t* addr_mode,
                         mem_t* operands[])
    {
        assert(opd_count <= MAX_OPERANDS);
        for (size_t i = 0; i < opd_count; ++i) {
            mem_t* raw = &(m_memory[m_pc++]);
            switch (addr_mode[i]) {
            case 0:
                operands[i] = &(m_memory[*raw]);
                break;
            case 1:
                operands[i] = raw;
                break;
            case 2:
                operands[i] = &(m_memory[*raw + m_relbase]);
                break;
            default:
                assert(false);
                break;
            }
        }
    }

    static void debug_instr(const mem_t instruction,
                            const size_t opd_count,
                            const mem_t* const addr_mode,
                            const mem_t* const operands[])
    {
        cerr << "instr " << instruction << " = " << (instruction % 100) << "/";
        assert(opd_count <= MAX_OPERANDS);
        for (size_t i = 0; i < opd_count; ++i) {
            if (i > 0) {
                cerr << ".";
            }
            cerr << addr_mode[i];
        }
        cerr << " (";
        for (size_t i = 0; i < opd_count; ++i) {
            if (i > 0) {
                cerr << ",";
            }
            cerr << *(operands[i]);
        }
        cerr << ") ";
    }

private:
    size_t m_pc = 0;
    size_t m_relbase = 0;
    size_t m_length = 0;
    size_t m_size = 0;
    mem_t* m_memory = nullptr;
    state_t m_state = INIT;

    static constexpr size_t MAX_OPERANDS = 3;
    static constexpr size_t EXTRA_MEM = 10000;
};


int main(const int argc, const char* argv[])
{
    constexpr bool DEBUG = false;

    Program prog;
    prog.read(argv[1]);
    prog.run_interactive(DEBUG);

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

