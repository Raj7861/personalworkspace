#include <stdio.h>

#define MAX 20

#define PI 3.1415

#define print printf("PRINT THIS!\n")
#define SUM(a, b) (a < 0 ? a + b : -1) 

int main()
{
    printf("Max: %d\n", SUM(4, -6));

    print;

    return 0;
}