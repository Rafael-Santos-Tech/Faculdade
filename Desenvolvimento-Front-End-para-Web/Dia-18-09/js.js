//localizar o botão

let botao = document.getElementById("meuBotão");

// criar um evento

botao.addEventListener("click", function(){
    // localizar o paragrafo

    let mensagem = document.getElementById("mensagem");

    mensagem.innerHTML = "Você clicou no botão";
});