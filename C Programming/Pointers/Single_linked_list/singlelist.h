typedef struct Node
{
    int data;
    struct Node *next;
} Node;

void insertbeggining(int data);
void insert_end(Node *node, int data);
void printlist(Node *current);
int listlength(Node *head);
void add_at_position(int data, int pos);
void delete(int pos);
void is_contain(int data);
