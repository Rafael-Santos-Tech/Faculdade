#include <stdio.h>

int main()
{
    int rgm;
    float media,nota_1,nota_2;
    printf("Insira o RGM e informe a nota da A1 e a nota da A2.\n");
    printf("RGM: ");
    scanf("%d",&rgm);
    printf("Nota da A1: ");
    scanf("%f",&nota_1);
    printf("Nota da A2: ");
    scanf("%f",&nota_2);
    media = (nota_1 * nota_2) / 2;
    printf("O estudante de RGM %d tem uma media de %.2f\n", rgm,media);
    
    return 0;
}