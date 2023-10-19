#include <stdlib.h>
#include <stdio.h>
#include "singlelist.h"

Node *head = NULL;

int main(){


    insertbeggining(500);
    insert_end(head, 90000);
    insertbeggining(400);
    insertbeggining(300);
    insertbeggining(200);
    add_at_position(700, 5);
    add_at_position(600, 5);
    // printf("\n AFTER\n");
     
    add_at_position(100, 1);
    // is_contain(2000);
    listlength(head);
    printlist(head);

    return 0;
}

void insertbeggining(int data){
    
    Node *newNode = (Node *)(malloc(sizeof(Node)));
    newNode->data = data;
    newNode->next = head;
    head = newNode;
}
void insert_end(Node *current, int data){
    Node *newNode = (Node *)(malloc(sizeof(Node)));
    newNode->data = data;
    newNode->next = NULL;

    while (current-> next != NULL)
    {
        current = current->next;
    }
    current->next = newNode;
    
}
int listlength(Node *head)
{
    int count = 0;

    while (head->next != NULL)
    {
        count = count + 1;
        head = head->next;
    }
    count = count + 1;
    
    return count;
}

void add_at_position(int data, int pos)
{

    Node *newNode = (Node *)(malloc(sizeof(Node)));
    newNode->data = data;
    newNode->next = NULL;

    int length = listlength(head);

    if(pos  > length + 1){
        printf("Invalid positon: The list contains %d nodes\n", length);
        return;
    }
    if(pos == 1){
        insertbeggining(data);
        return;
    }
    else if (pos == length + 1)
    {
        insert_end(head, data);
        return;
    }else{
        Node *ptr = head;

        while (pos - 1 != 1)
        {
           // printf("PTR -> %d , Node -> %d, %p\n", pos, ptr->data, ptr->next);
            ptr = ptr->next;
            pos--;
        }
        //printf("PTR -> %d , Node -> %d, %p\n", pos, ptr->data, ptr->next);
        newNode->next = ptr->next;
        ptr->next = newNode;
    }
}
void is_contain(int data){
    char *s = "FALSE";
    while (head->next != NULL)
    {
        if (head->data == data)
        {
            s = "TRUE";
            break;
        }
        else
        {
            head = head->next;
        }
    }
        printf("%s\n", s);
}
void delete(int pos){
        int len = listlength(head);
        if(pos > len){
            printf("Invalid position");
        return;
        }
        while (pos - 1 != 1)
        {
            
        }
        
}

void printlist(Node *node)
{
    int i;
    for (i = 1; node->next != NULL; i++)
    {
        printf("Node [%d]: %d \n", i, node->data);
        node = node->next;
    }
    printf("Node [%d]: %d \n", i, node->data);
}
