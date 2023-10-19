#include <stdlib.h>
#include <stdio.h>
#include "listh.h"



int main(){
    Node *head = NULL;
    head = insert_beg(head,600);
    insert_end(head, 300);
    insert_end(head, 400);
    head = insert_beg(head, 1000);

    print_list(head);
    printf("The length = %d\n", len(head));
    return 0;
    }

void remove(Node *head){
    Node *current = head;
    
    if(current->next == NULL)
}

void insert_end(Node *head, int data)
{

    Node *newNode = (Node *)(malloc(sizeof(Node)));

    newNode->data = data;
    newNode->next = NULL;

    while (head->next != NULL)
    {
        head = head->next;
    }
    head->next = newNode;

}

Node *insert_beg(Node *head, int data)
{
    Node* node1 = (Node *)(malloc(sizeof(Node)));
    node1->data = data;
    node1->next = head;
    head = node1;

    return head;
}

int len(Node *head){

    int count = 0;
    Node *current = head;
    while (current->next != NULL)
    {
        count = count + 1;
        current = current->next;
    }
    count = count + 1;
    return count;
}

void print_list(Node * head)
    {

        int i;

        for (i = 1; head->next != NULL; i++)
        {
            printf("Node [%d]: Data: %d\n", i, head->data);
            head = head->next;
        }
        printf("Node [%d]: Data: %d\n", i, head->data);
 }
