#include <stdio.h>
#include <stdlib.h>

void exibirVetor(int vetor[], int tamanho){
    for(int i = 0; i < tamanho; i++){
        printf("{%d} ", vetor[i]);
    }
    printf("\n");
}

void bubbleSort(int vetor[], int tamanho){
    int auxiliar;

    for(int i = 0; i < tamanho - 1; i++){
        for(int j = 0; j < tamanho -1 -i; j++){
            if(vetor[j] > vetor[j + 1]){
                auxiliar = vetor[j];
                vetor[j] = vetor[j + 1];
                vetor[j + 1] = auxiliar;
            }
        }
    }
}

int main(void){
    int senhas[5] = {35, 12, 28, 7, 19};
    int tamanho = 5;
    printf("Senhas Antes: \n");
    exibirVetor(senhas, tamanho);
    printf("Senhas depois da ordenação: \n");
    bubbleSort(senhas, tamanho);
    exibirVetor(senhas, tamanho);
}

