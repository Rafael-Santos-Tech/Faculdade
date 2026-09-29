/*
============================================================
PROJETO: MISSÃO ORBITAL
DISCIPLINA: ALGORITMOS E PENSAMENTO COMPUTACIONAL

            Online C Compiler.
Autores do projeto:
Rafael dos Santos Ferreira Lima RGM: 47596295
Nathan Umbelino do Carmo RGM: 47719567
Cauã Correia de Andrade RGM: 47766875
Eloysa Raquel dos Santos RGM: 47700971


DESCRIÇÃO:
Sistema desenvolvido em linguagem C para cadastrar as
pontuações de um cadete, calcular a pontuação total,
calcular a média e apresentar sua classificação.

============================================================
*/
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    char nomeNave[50];
    char codigoMissao[20];
    int codigoCadete, etapa, pontos, continuar;
    float media;
    
    printf("===== CONFIGURAÇÃO DA MISSÃO =====\n");
    printf("Digite o nome da nave: ");
    scanf(" %[^\n]", nomeNave);

    printf("Digite o código da missão: ");
    scanf(" %[^\n]", codigoMissao);

    do {
        printf("\n===== MISSÃO ORBITAL =====\n");
        printf ("Digite o código do cadete: ");
        scanf("%d", &codigoCadete);

        int total = 0;
        int etapasAcima80 = 0;
        int maiorPontuacao = -1;
        int menorPontuacao = 101;

        for (etapa = 1; etapa <= 3; etapa++){

            printf("Digite a pontuação da etapa %d: ", etapa);
            scanf("%d", &pontos);

            while(pontos < 0 || pontos > 100){
                printf("Pontuação inválida! Digite novamente a pontuação (0 a 100): ");
                scanf("%d", &pontos);
            }

        total += pontos;

        if (pontos >= 80) {
                etapasAcima80++;
        }

        if (pontos > maiorPontuacao) {
                maiorPontuacao = pontos;
        }

        if (pontos < menorPontuacao) {
                menorPontuacao = pontos;
        }

        if(total == 300){
            printf("\n-------------------------------\n");
            printf("Pontuação máxima!");
            printf("\n-------------------------------\n");
        }
        }

        media = total / 3.0f;

        printf("\n---------- RESULTADO ---------\n");
        printf("Nave: %s\n", nomeNave);
        printf("Código da Missão: %s\n", codigoMissao);
        printf("Cadete: %d\n", codigoCadete);
        printf("Pontuação Total: %d\n", total);
        printf("Média: %.2f\n", media);
        printf("Etapas com pontuação >= 80: %d\n", etapasAcima80);
        printf("Maior pontuação: %d\n", maiorPontuacao);
        printf("Menor pontuação: %d\n", menorPontuacao);

        if(media >= 85.0){
            printf("Treinamento concluído com excelência.\nClassificação: (Comandante da missão)");
        }
        else if (media >= 70.0){
            printf("Cadete autorizado para a missão.\nClassificação: (Piloto aprovado)");
        }
        else if (media >= 50.0){
            printf("Novo treinamento recomendado.\nClassificação: (Cadete em recuperação)");
        }
        else {
            printf("Cadete ainda não autorizado.\nClassificação: (Treinamento reiniciado)");
        }
        printf("\n-------------------------------\n");

        printf("Deseja avaliar outro cadete? (0 - não | 1 - sim): ");
        scanf("%d", &continuar);

    }   while (continuar == 1);
    
    return 0;
}