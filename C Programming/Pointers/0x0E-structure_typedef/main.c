#include <stdio.h>

int main()
{
    // Write C code here

    int n = 98;

    int *pointer = &n;
    n = 20000;
    printf("%d Hello world\n", *pointer);

    return 0;
}


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self, data) -> None:
        self.head = Node(data)

    def insert_beg(self,data) -> Node:
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def insert_end(self, data: int):
        new_node = Node(data)
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = new_node

    def print_node(self):
        curr = self.head
        while curr.next != None:
            print(curr.data)
            curr = curr.next
        print(curr.data)