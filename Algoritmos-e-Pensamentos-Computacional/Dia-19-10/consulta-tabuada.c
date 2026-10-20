#include <stdio.h>
#include <stdlib.h>

int main (){

    FILE *arquivo;
    char linha[100];

    arquivo = fopen ("tabuada.txt", "r");

    if (arquivo == NULL){
        printf("Não foi possível ler o arquivo.\n");
        return 1;
    }

    printf("Conteúdo do arquivo: \n");

    while(fgets(linha, sizeof(linha), arquivo) != NULL){
        printf("%s", linha);
    }

    fclose(arquivo);

    return 0;
}