#include <stdio.h>
#include <stdlib.h>

int main (){

    int idade[5] = {20, 24, 18, 19, 31};

    for (int i = 0; i < 5; i++)
    {
        printf("A idade da posição %d: %d anos\n",i+1, idade[i]);
    }
    return 0;
}