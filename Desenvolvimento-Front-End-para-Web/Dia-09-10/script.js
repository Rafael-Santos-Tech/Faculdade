const botoes = document.querySelectorAll("button");
const mensagem = document.getElementById("mensagem");
botoes.forEach(function (botao){
    botao.addEventListener("click", function(){
        mensagem.textContent = "Você clicou no botão: " +
        botao.textContent.trim();
    });
});