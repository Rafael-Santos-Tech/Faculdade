#include <stdio.h>

int main()
{
    
    float frequencia, media;
    float nota1, nota2;
    
    printf("Digite a primeira nota: ");
    scanf("%f",&nota1);

    printf("Digite a segunda nota: ");
    scanf("%f",&nota2);

    printf("Digite o percentual de frequência? ");
    scanf("%f",&frequencia);
    
    media = (nota1 + nota2) / 2.0f;
    
    if (frequencia >= 75) {
        if (media >= 6) {
            printf("Aluno aprovado parabéns :)");
            printf("\nFrequência=%.2f%\nMédia=%.2f", frequencia, media);
        }
        
        else {
            printf("Aluno foi aprovado por frequência mas, reprovado por nota :(");
            printf("\nFrequência=%.2f%\nMédia=%.2f", frequencia, media);
        }
        
    } else {
        if (media >= 6) {
            printf("Aluno reprovado por falta mas, foi aprovado por nota, infelizmente :(");
            printf("\nFrequência=%.2f%\nMédia=%.2f", frequencia, media);
        }
        else {
            printf("Aluno foi reprovado por falta e media, infelizmente o incompetente não conseguiu nem trazer felicidade a própria mãe !!!");
            printf("\nFrequência=%.2f%\nMédia=%.2f", frequencia, media);
        }
    }
    

    return 0;
}