#include <stdio.h>
#include <stdarg.h>

// function prototype
int add(int arg, ...);

int main(){
    printf("Addition 1 = %d\n", add(5, 1, 2, 3, 4, 5));
     return 0;
}

// add function which is a variadic function

int add(int args, ...){
    va_list list;

    va_start(list, args);
    // all actions will be placed here.
    int i, sum = 0;
    for (i = 0; i < args; i++){
        sum += va_arg(list, int);
    }

        va_end(list);

        return sum;
}