#include <stdio.h>
#include <math.h>

int main() 
{
    int qtd_caixas;
    float largura, comprimento, valor, area_total, custo_total, caixa = 2.5;
    
    printf ("Qual é a largura da área (em metros)? ");
    scanf ("%f", &largura);
    printf ("Qual é o comprimento da área em metros? ");
    scanf ("%f", &comprimento);
    printf("Qual é o valor de cada caixa? ");
    scanf ("%f", &valor);
    area_total = largura * comprimento;
    qtd_caixas = ceil(area_total / caixa);
    custo_total = valor * qtd_caixas;
    printf ("Área total a ser revestida: %.2f m^2\nQuantidade de caixas necessárias: %d\nCusto total da compra: R$ %.2f", area_total, qtd_caixas, custo_total);
    return 0;
}