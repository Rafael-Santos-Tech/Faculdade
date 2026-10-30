function somarVarios() {
    let numeros = []; // Array vazio para guardar os valores
    let continuar = true; // Variável de controle do laço

    // Laço de repetição infinito até o usuário digitar 's'
    while (continuar) {
        let entrada = window.prompt("Digite um número (ou 's' para parar):");

        // Verifica se a entrada é a letra 's' (minúscula ou maiúscula)
        if (entrada === 's' || entrada === 'S') {
            continuar = false; // Quebra o laço
        } else {
            let num = parseInt(entrada);

            // Valida se o que foi digitado realmente é um número antes de colocar no array
            if (!isNaN(num)) {
                numeros.push(num); // Adiciona o número ao array
            } else {
                window.alert("Valor inválido! Digite um número válido ou 's' para sair.");
                    }
        }
    }

    // Calcula a soma dos números que estão no array
    let soma = 0;
    for (let i = 0; i < numeros.length; i++) {
                soma = soma + numeros[i];
    }

    // Exibe os números informados e o resultado
    window.alert(`Números digitados: ${numeros.join(', ')}\nA soma total é: ${soma}`);
}