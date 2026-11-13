#include <stdio.h>
#include <stdlib.h>

void exibirNotas(float notas[], int tamanho){
    for(int i = 0; i < tamanho; i++){
        printf("{%.2f} ", notas[i]);
    }
    printf("\n");
}

void ordenarNotas(float notas[], int tamanho){
    float auxiliar;

    for(int i = 0; i < tamanho - 1; i++){
        for(int j = 0; j < tamanho -1 -i; j++){
            if(notas[j] < notas[j + 1]){
                auxiliar = notas[j];
                notas[j] = notas[j + 1];
                notas[j + 1] = auxiliar;
            }
        }
    }
}


int main(void){
    float notas[5] = {6.5, 9.0, 7.5, 5.0, 8.0};
    int tamanho = 5;
    printf("Notas: \n");
    exibirNotas(notas, tamanho);
    ordenarNotas(notas, tamanho);
    printf("Notas Organizadas: \n");
    exibirNotas(notas, tamanho);
}