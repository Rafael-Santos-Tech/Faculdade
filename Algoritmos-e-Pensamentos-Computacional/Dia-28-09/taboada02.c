#include <stdio.h>
#include <stdlib.h>

int main(){
    int numero, i;

    printf("Digite um número inteiro: ");
    scanf("%d", &numero);

    for(i=0; i<=10; i++){
        printf("Numero: %d\n", numero*i);
    }
    return 0;
}