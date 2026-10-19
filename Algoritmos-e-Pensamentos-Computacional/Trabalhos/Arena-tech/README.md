# 🏟️ Arena Tech | Dimensionamento de Infraestrutura

O **Arena Tech** é um algoritmo desenvolvido em **C** para automatizar o planejamento e o cálculo de infraestrutura de grandes eventos de tecnologia.

O objetivo principal do sistema é aplicar lógica matemática para garantir que os organizadores tenham estimativas precisas de custos e consumo, evitando desperdícios financeiros e sobrecarga do sistema elétrico.

### ⚙️ Funcionalidades e Regras de Negócio
- **Cálculo de Consumo:** Estima o consumo de energia elétrica (em kWh) com base na quantidade de computadores e no tempo de duração do evento.
- **Gestão de Custos:** Calcula o custo total de operação do evento, agrupando despesas de consumo e de estrutura.
- **Dimensionamento de Equipamentos:** Automatiza a contagem e os custos de locação de equipamentos necessários de acordo com o número de equipes participantes.

### 🛠️ Tecnologias Utilizadas
- **Linguagem:** `Linguagem C`
- **Conceitos:** `Lógica Matemática`, `Estruturas Condicionais`, `Processamento de Dados`
- **Compilador:** `GCC / MinGW`

### 🚀 Como testar o código
Certifique-se de ter um compilador C instalado na sua máquina. Abra o terminal na pasta do arquivo e execute os comandos:
```bash
gcc nome_do_arquivo.c -o arena_tech
./arena_tech