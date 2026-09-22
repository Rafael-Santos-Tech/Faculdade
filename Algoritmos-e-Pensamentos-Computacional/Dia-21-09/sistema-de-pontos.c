#include <stdio.h>

int main()
{
    int rodada = 1; 
    int pontuacao;
    int total = 0;
    
    while (rodada <= 3){
        printf("Digite os pontos da rodada %d: \n", rodada);
        scanf("%d", &pontuacao);
        
        rodada++;
        total = total + pontuacao;
        
    }
    
    printf("O valor total de pontos é: %d\n", total);
    return 0;
}
