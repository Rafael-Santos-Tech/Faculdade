#include <stdio.h>
#include <stdlib.h>

int main (){

    int vendas[3][4];
    int i, j;

    for (i = 0; i < 3; i++)
    {
        for (j = 0; j < 4; j++)
        {
            printf("Digite o valor da venda [%d][%d] funcionário: \n",i+1, j+1);
            scanf("%d", &vendas[i][j]);
        }  
    }
    
    for (i = 0; i < 3; i++)
    {
        for (j = 0; j < 4; j++){
            printf("O valor da venda [%d][%d] é: %d\n", i+1, j+1, vendas[i][j]);
        }
    }

    return 0;
}