#include <stdio.h>

int main() 
{
    int potencia, horas;
    float consumo;
    
    printf ("Potência do equipamento (w)? ");
    scanf ("%d", &potencia);
    printf ("Horas de uso por dia? ");
    scanf ("%d", &horas);
    consumo = (float)(potencia*horas*30)/1000;
    printf ("Consumo mensal: %.2f kWh", consumo);
    return 0;
}