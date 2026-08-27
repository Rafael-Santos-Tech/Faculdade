#include <stdio.h>
#define PI 3.141

int main()
{
    float raio = 5.30, perimetro;
    
    printf("Qual a medida do raio (em cm)? ");
    scanf("%f", &raio);
    perimetro = 2 * PI * raio;
    printf("O perímetro da circunferência é %.2fcm.\n", perimetro);
    
    return 0;
}