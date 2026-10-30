// Seleciona o elemento h1
const titulo = document.getElementById("meuTitulo");

function alterarTitulo() {
    // Pede um novo texto ao usuário pelo prompt
    let novoTexto = window.prompt("Qual deve ser o novo título?");
            
    // Se o usuário digitar algo e não clicar em cancelar, altera o texto
    if (novoTexto !== null && novoTexto.trim() !== "") {
        titulo.innerText = novoTexto;
    }
}

function alterarCorFundo() {
    // Array com algumas cores pastéis para combinar com o layout
    const cores = ["#ffe4e1", "#e0ffff", "#f0fff0", "#fffacd", "#e6e6fa", "#ffdab9"];
            
    // Sorteia uma cor aleatória do array
    let corSorteada = cores[Math.floor(Math.random() * cores.length)];
            
    // Aplica a cor sorteada ao fundo do body
    document.body.style.backgroundColor = corSorteada;
}