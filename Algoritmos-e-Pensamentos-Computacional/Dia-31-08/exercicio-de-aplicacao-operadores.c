#include <stdio.h>

int main() 
{
    float kg, altura, imc;
    
    printf ("Qual é o peso da pessoa em kg? ");
    scanf ("%f", &kg);
    printf ("Qual é a altura da pessoa em metros? ");
    scanf ("%f", &altura);
    imc = kg / (altura*altura);
    printf ("O Índice de Massa Corporal é %.2f kg/m^2", imc);
    return 0;
}