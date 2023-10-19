#include <stdio.h>
#include <stddef.h>
#include <stdlib.h>

#include "dog.h"

/**
 * @brief init_dog - initialize dog struct
 * 
 * @d: input pointer to struct dog
 * @name: input name for the dog
 * @age: input for dog age
 * @owner: input for dog owner
 * 
 */

void init_dog(struct dog *d, char *name, float age, char *owner)
{
    if(d)
    {
        d->name = name;
        d->age = age;
        d->owner = owner;
    }
}

int main(){

    dog_t dog1;

    init_dog(&dog1, "Snoopy", 0.5, "Siraj");
    dog1.name = "CRY";
    // init_dog(&dog1, "Sny", 0.5, "Siraj");

    printf("Do name is %s\n", dog1.name);

    return 0;
}