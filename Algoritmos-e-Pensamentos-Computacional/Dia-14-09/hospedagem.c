#include <stdio.h>

int main()
{
    
    char tipoHospedagem;
    int qtdDiarias;
    float valorDiarias, valorTotal;
    
    printf("Qual o tipo de Hospedagem (S - D - T)? ");
    scanf("%c",&tipoHospedagem);

    printf("Qual a quantidade de diarias? ");
    scanf("%d",&qtdDiarias);

    switch(tipoHospedagem){
        case 'S':
        case 's':
            valorDiarias = 300.0f;
            break;
        case 'D':
        case 'd':
            valorDiarias = 450.0f;
            break;
        case 'T':
        case 't':
            valorDiarias = 500.0f;
            break;
        
        default:
            printf("\n Tipo Inválido\n");
    }
    
    valorTotal = valorDiarias * qtdDiarias;
    
    printf("\n O valor Total da Hospedagem é: R$%.2f", valorTotal);

    return 0;
}