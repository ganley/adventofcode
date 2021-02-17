#include <assert.h>
#include <iostream>

using namespace std;


// linked list node
class Node
{
   public:
    Node(const int label)
    :   m_label(label),
        m_next(nullptr)
    {
    }

    int m_label;
    Node* m_next;
};


Node* nodes[10000002];


Node* go(const string& txt, const int num_moves)
{
    // fill the first N from the string
    for (int i = 1; i <= txt.length(); ++i) {
        nodes[i] = new Node(txt[i - 1] - '0');
    }
    // fill the rest with ascending integers
    for (int i = txt.length() + 1; i <= 1000000; i++) {
        nodes[i] = new Node(i);
    }
    const int max = 1000000;

    // build the linked list
    for (int i = 1; i <= 999999; i++) {
        nodes[i]->m_next = nodes[i + 1];
    }
    nodes[1000000]->m_next = nodes[1];

    // index the first 9 (since their label doesn't match their index)
    int ix[10];
    for (int i = 1; i <= 9; ++i) {
        ix[nodes[i]->m_label] = i;
    }

    // do the thing
    Node* curr = nodes[1];
    for (int m = 1; m <= num_moves; ++m) {
        Node* pull = curr->m_next;
        const Node* pull2 = pull->m_next;
        Node* pull3 = pull2->m_next;
        Node* after_pull = pull3->m_next;

        // remove pulled sub-list
        curr->m_next = after_pull;

        // find the destination label
        int dest = curr->m_label > 1 ? curr->m_label - 1 : max;
        while (dest == pull->m_label || dest == pull2->m_label ||
               dest == pull3->m_label) {
            --dest;
            if (dest < 1) {
                dest = max;
            }
        }

        // find the destination index (different if it's one of the first 9)
        int dest_ix = dest;
        if (dest < 10) {
            dest_ix = ix[dest];
        }

        // reinsert the pulled sub-list after the destination
        Node* dest_node = nodes[dest_ix];
        assert(dest_node->m_label == dest);
        Node* after_dest = dest_node->m_next;
        dest_node->m_next = pull;
        pull3->m_next = after_dest;

        // advance the current cup
        curr = curr->m_next;
    }

    // return the node labeled "1"
    return (nodes[ix[1]]);
}


int main(int argc, char* argv[])
{
    const int num_moves = 10000000;
    //const string txt("389125467");     // sample
    const string txt("123487596");  // input

    const Node* curr = go(txt, num_moves);

    cout << (static_cast<long unsigned int>(curr->m_next->m_label) *
             static_cast<long unsigned int>(curr->m_next->m_next->m_label))
         << "\n";
}

