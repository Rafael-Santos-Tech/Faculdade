#include <stdio.h>
#include <math.h>

int main ()
{
    int participantes,jogadoresPorTime, computadores, qtd_times;
    float potencia, duracao, precoKwH, precoKit, outrosCustos, consumoEnergia, custoEnergia, custoAlimentacao, custoTotal, custoPorParticipante;
    
    printf ("Qual o total de participantes? ");
    scanf ("%d", &participantes);
    printf ("Quantos jogadores em cada time? ");
    scanf ("%d", &jogadoresPorTime);
    printf ("Quantidade de computadores utilizados? ");
    scanf ("%d", &computadores);
    printf ("Potência média de cada computador em (watts)? ");
    scanf ("%f", &potencia);
    printf ("Duração do evento em (horas)? ");
    scanf ("%f", &duracao);
    printf ("Preço de 1 kWh de energia? ");
    scanf ("%f", &precoKwH);
    printf ("Preço de um kit de alimentação por participante: ");
    scanf ("%f", &precoKit);
    printf ("Outros custos do evento: ");
    scanf ("%f", &outrosCustos);
    qtd_times = ceil((float)participantes / jogadoresPorTime);
    consumoEnergia = (computadores * potencia * duracao)/1000;
    custoEnergia = consumoEnergia * precoKwH;
    custoAlimentacao = participantes * precoKit;
    custoTotal = custoEnergia + custoAlimentacao + outrosCustos;
    custoPorParticipante = custoTotal / participantes;
    printf ("========== ARENA TECH ==========\nTotal de participantes: %d\nTimes necessários: %d\nConsumo estimado: %.2f kWh\nCusto da energia: R$ %.2f\nCusto de alimentação: R$ %.2f\nOutros custos: R$ %.2f\nCusto Total: R$ %.2f\nCusto por Participante: R$ %.2f\n================================", participantes, qtd_times, consumoEnergia, custoEnergia, custoAlimentacao, outrosCustos, custoTotal, custoPorParticipante);
    return 0;
}
