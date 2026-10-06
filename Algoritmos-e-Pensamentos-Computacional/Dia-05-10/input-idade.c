#include <stdio.h>
#include <stdlib.h>

int main (){

    int idade[5] = {0};

    for (int i = 0; i < 5; i++)
    {
        printf("\nDigite o valor da posição %d: ", i+1);
        scanf("%d", &idade[i]);
    }

    for (int i = 0; i < 5; i++)
    {
        printf("\nA idade da posição %d: %d anos", i+1, idade[i]);
    }

    return 0;
}