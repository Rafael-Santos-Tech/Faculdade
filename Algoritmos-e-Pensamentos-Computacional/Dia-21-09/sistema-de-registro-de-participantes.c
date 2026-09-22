#include <stdio.h>

int main()
{
    int participantes;
    
    do {
        printf("Digite a quantidade de pessoas no grupo: ");
        scanf("%d", &participantes);
        if (participantes < 1 || participantes > 3){
            printf("Número de participantes invalido.\n");
        }
    }
    
    while (participantes < 1 || participantes > 3);
    
    printf("Equipe registrada com: %d participantes.\n", participantes);
    return 0;
}
