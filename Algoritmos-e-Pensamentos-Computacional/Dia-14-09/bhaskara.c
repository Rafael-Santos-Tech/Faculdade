#include <stdio.h>
#include <math.h>

int main()
{
    float a, b, c;
    float x1, x2, delta;
    printf("Digite o valor de A: ");
    scanf("%f",&a);
    
    printf("Digite o valor de B: ");
    scanf("%f",&b);
    
    printf("Digite o valor de C: ");
    scanf("%f",&c);
    
    delta = b*b -4 * a * c;
    x1 = (-b - sqrtf(delta)) / 2 * a;
    x2 = (-b + sqrtf(delta)) / 2 * a;
    
    printf("O valor da raiz é:\nX1= %.2f\nX2= %.2f", x1, x2);
    
    
    return 0;
}