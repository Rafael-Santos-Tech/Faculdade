#include <stdio.h>
#include <stdlib.h>

int main (){

    int qtd, i;
    FILE *arquivo;
    char dia[10];
    float consumo;

    arquivo = fopen ("consumo.txt", "a");

    if (arquivo == NULL){
        printf("Não foi possível criar o arquivo.\n");
        return 1;
    }

    printf("Quantos registros deseja cadastrar? ");
    scanf("%d", &qtd);

    for(i=1; i<=qtd; i++){
        printf("\n Registro %d \n", i);

        printf("Dia da semana: ");
        scanf("%9s", dia);

        printf("Consumo: ");
        scanf("%f", &consumo);

        fprintf(arquivo, "%s %.2f\n", dia, consumo);
    }

    fclose(arquivo);

    printf("Consumo diário gravada com sucesso :)");

    return 0;
}