#include <stdio.h>
#include <stdlib.h>

int main (){

    float valores[8] = {0};
    float soma = 0.0f, media;
    int acimaMedia = 0;
    
    for (int i = 0; i < 8; i++)
    {
        printf("\nDigite o valor %dº: ", i+1);
        scanf("%f", &valores[i]);
        soma += valores[i];
    }

    media = soma / 8;

    for(int i = 0; i < 8; i++){
        if (valores[i] > media){
            acimaMedia ++;
        }
    }

    printf("A média dos valores é: %.2f \nValores acima da média: %d\n", media, acimaMedia);

    return 0;
}