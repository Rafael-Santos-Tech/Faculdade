#include <stdio.h>
#include <stdlib.h>

int main (){

    char cpf [15];
    double preco, soma = 0.0;

    printf("Digite o CPF: ");
    scanf("%14s", cpf);

    do
    {
        printf("Digite o valor do produto ou 0 para finalizar: R$ ");
        scanf("%lf", &preco);

        if(preco > 0){
            soma += preco;
        }
        
    } while (preco != 0);

    printf("CPF: %s\nResultado: R$ %.2lf\n", cpf, soma);
    
    return 0;
}