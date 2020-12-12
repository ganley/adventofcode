#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

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

    vector<string> prog_tokens = tokenize(prog_str, ",");
    length = prog_tokens.size();
    program = new int[length];
    for (size_t i = 0; i < length; ++i) {
        program[i] = atoi(prog_tokens[i].c_str());
    }
}

void run_intcode(int* program, const size_t length)
{
    size_t pc = 0;
    while (pc < length && program[pc] != 99) {
        const size_t src_addr1 = program[pc + 1];
        const size_t src_addr2 = program[pc + 2];
        const size_t dst_addr = program[pc + 3];
        const int opd1 = program[src_addr2];
        const int opd2 = program[src_addr2];
        switch (program[pc]) {
            case 1:
                program[dst_addr] = program[src_addr1] + program[src_addr2];
                break;
            case 2:
                program[dst_addr] = program[src_addr1] * program[src_addr2];
                break;
            default:
                cerr << "bad instruction: " << program[pc] << "\n";
                exit(-1);
        }
        pc += 4;
    }
}

int main(const int argc, const char* argv[])
{
    int* program;
    size_t length;
    read_intcode(argv[1], program, length);
    run_intcode(program, length);

    // for (size_t i = 0; i < length; ++i) {
    //    cout << program[i] << " ";
    //}
    // cout << "\n";
    cout << program[0] << endl;

    exit(0);
}
