#include <stdio.h>

int add(int a, int b){
    return a + b;
}

int main()
{
   // int *ptr[10]; // array of 10 integer pointers
    //int(*ptr)[10] // ptr is a pointer to an array of 10 integers.
    //int (*ptr)(int, int) // ptr is a pointer to a function containing two integer arguments and it returns an inger

    int (*ptr)(int, int) = add;

    int results = ptr(10, 20);
    printf("%d\n", results);
}