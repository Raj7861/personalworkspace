#ifndef SINGLE_H
#define SINGLE_H

typedef struct Node
{
    int data;
    struct Node *next;
} Node;

Node *insert_beg(Node *head, int data);
void insert_end(Node *current, int data);
void print_list(Node *current);
int len(Node *head);
void remove(Node *head);

#endif