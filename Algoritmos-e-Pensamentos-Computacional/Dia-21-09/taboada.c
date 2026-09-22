#include <stdio.h>
#include <stdlib.h>

int main()
{
    int  numero, contador, qtd;
    
    printf ("Digite o número da taboada: ");
    scanf("%d", &numero);
    printf ("Digite até qual número deseja que seja calculado na taboada: ");
    scanf("%d", &qtd);
    
    for (contador = 1; contador <= qtd; contador++){
        numero * contador;
        printf("%d * %d = %d\n", numero, contador, numero*contador);
    }
    
    system("pause");
    return 0;
}
