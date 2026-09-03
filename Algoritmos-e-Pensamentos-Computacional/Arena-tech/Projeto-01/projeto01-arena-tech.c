#include <stdio.h>
#include <math.h>

#define capacidadeFiltro 5

int main ()
{
    char nomeEvento[50] = "ARENA TECH";
    char dataEvento[10] = "08/09/2026";
    char organizador[100] = "";
    
    
    int participantes,jogadoresPorTime, computadores, qtdTimes, diasCenario1, diasCenario2, filtrosNecessarios;
    float potencia, duracao, precoKwH, precoKit, outrosCustos, consumoEnergia, custoEnergia, custoAlimentacao, custoPorParticipanteCenario1, custoPorParticipanteCenario2, custoAluguelPcDia, custoAluguelCenario1, custoAluguelCenario2, custoTotalCenario1, custoTotalCenario2, diferencaCenarios;
    
    
    // Entrada
    printf ("=== %s Configuração do Evento ===\n", nomeEvento);
    
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
    
    printf ("Custo diario do aluguel de 1 PC (R$): ");
    scanf("%f", &custoAluguelPcDia);
    
    printf ("Outros custos do evento: ");
    scanf ("%f", &outrosCustos);
    
    printf("\n=== CENARIOS DE DURACAO DO EVENTO ===\n");
    
    printf("Duracao do Cenario 1 (em dias): ");
    scanf("%d", &diasCenario1);
    
    printf("Duracao do Cenario 2 (em dias): ");
    scanf("%d", &diasCenario2);
    
    // Calculos
    qtdTimes = ceil((float)participantes / jogadoresPorTime);
    
    filtrosNecessarios = ceil((double)computadores / capacidadeFiltro);
    
    consumoEnergia = (computadores * potencia * duracao)/1000;
    custoEnergia = consumoEnergia * precoKwH;
    
    custoAlimentacao = participantes * precoKit;
    
    custoAluguelCenario1 = computadores * custoAluguelPcDia * diasCenario1;
    custoAluguelCenario2 = computadores * custoAluguelPcDia * diasCenario2;
    
    custoTotalCenario1 = (custoEnergia * diasCenario1) + custoAlimentacao + outrosCustos + custoAluguelCenario1;
    custoTotalCenario2 = (custoEnergia * diasCenario2) + custoAlimentacao + outrosCustos + custoAluguelCenario2;
    
    custoPorParticipanteCenario1 = custoTotalCenario1 / participantes;
    custoPorParticipanteCenario2 = custoTotalCenario2 / participantes;
    
    diferencaCenarios = custoTotalCenario1 - custoTotalCenario2;
    
    // Saida
    printf ("\n==================================================\n                        %s                        \n==================================================\nData: %s | Organização: %s\n--------------------------------------------------\nResumo Operacional e Infraestrutura\n-Total de participantes: %d\n-Times necessários: %d\n-Computadores em uso: %d unidades\n-Tomadas necessarias %d\n-Filtros de Linha necessarios (%d tomadas/filtro): %d unidade(s)\n-Consumo de Energia diario estimado: %.2f kWh (R$ %.2f/dia)\n-Custo de alimentação: R$ %.2f\n-Outros custos: R$ %.2f\n--------------------------------------------------\nComparativo de Cenários de Duração\n  [Cenário 1 - %d Dia(s)]  \n-Aluguel dos PCs: R$ %.2f\n-Custo por participante: R$ %.2f\n-Custo Total do Evento: R$ %.2f\n  [Cenário 2 - %d Dia(s)]  \n-Aluguel dos PCs: R$ %.2f\n-Custo por participante: R$ %.2f\n-Custo Total do Evento: R$ %.2f\n--------------------------------------------------\nDiferença de custo total entre cenários: R$ %.2f\n==================================================\n",nomeEvento, dataEvento, organizador, participantes, qtdTimes, computadores, computadores, capacidadeFiltro, filtrosNecessarios, consumoEnergia, custoEnergia, custoAlimentacao, outrosCustos, diasCenario1, custoAluguelCenario1, custoPorParticipanteCenario1, custoTotalCenario1, diasCenario2, custoAluguelCenario2, custoPorParticipanteCenario2, custoTotalCenario2, diferencaCenarios);
    
    return 0;
}