#include <stdio.h>
#include <stdlib.h>

int main (){

    int qtd_aluno;
    float nota, media, soma = 0.0f;

    do
    {
        printf("Quantidade de alunos: ");
        scanf("%d", &qtd_aluno);

        if(qtd_aluno <= 0 ){
            printf("Quantidade inválida de alunos! \n");
        }

    } while (qtd_aluno <= 0);
    
    for (int i = 1; i <= qtd_aluno; i++){
        do
        {
            printf("Digite a nota do aluno %d: ", i);
            scanf("%f", &nota);

            if(nota < 0 || nota > 10){
                printf("Nota inválida\nDigite a nota novamente: ");
            }
        } while (nota < 0 || nota > 10);

        soma += nota;
        
    }

    media = soma / qtd_aluno;

    printf("A média de nota dos alunos desta turma é de: %.2f", media);

    return 0;
}