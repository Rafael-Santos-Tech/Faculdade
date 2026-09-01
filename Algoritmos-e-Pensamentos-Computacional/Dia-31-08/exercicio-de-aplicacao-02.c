#include <stdio.h>

int main() 
{
    int hora, minuto, total;
    
    printf ("Hora? ");
    scanf ("%d", &hora);
    printf ("Minutos? ");
    scanf ("%d", &minuto);
    total = hora*60+minuto;
    printf ("Já se passaram %d minutos desde o início do dia.", total);
    return 0;
}