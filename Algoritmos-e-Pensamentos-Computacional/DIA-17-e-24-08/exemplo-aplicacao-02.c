#include <stdio.h>

int main()
{
    int qtd_cafe;
    float valor_total, preco;
    
    printf("Quantos cafés você deseja? ");
    scanf("%d", &qtd_cafe);
    printf("Digite o valor do café: ");
    scanf("%f", &preco);
    valor_total = preco*qtd_cafe;
    printf("O valor da conta é de R$ %.2f.\n", valor_total);
    
    return 0;
}