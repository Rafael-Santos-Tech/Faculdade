#include <stdio.h>

int main()
{
    float nota1, nota2, media;
    
    printf("Digite a primeira nota: ");
    scanf("%f",&nota1);

    printf("Digite a segunda nota: ");
    scanf("%f",&nota2);

    media = (nota1 + nota2) / 2.0f;
    
    if (media >= 6) {
        printf("Parabéns! Você foi aprovado com média: %.2f", media);
    }
    else {
        printf("Você foi reprovado infelizmente, com média: %.2f", media);
    }
    

    return 0;
}