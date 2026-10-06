#include <stdio.h>
#include <stdlib.h>

int main (){

    float salario[4] = {0};

    for (int i = 0; i < 4; i++)
    {
        printf("\nDigite o salário do %dº funcionário: R$", i+1);
        scanf("%f", &salario[i]);
    }

    for (int i = 0; i < 4; i++)
    {
        printf("\nFuncionário %d: R$%.2f ", i+1, salario[i]);
    }

    return 0;
}