const perguntas = [
    {
        pergunta: "Qual palavra que usamos para variavel?",
        opcoes: ["var", "print", "echo", "write"],
        resposta: "var"
    }, 
    {
        pergunta: "Qual comando mostra algo no console?",
        opcoes: ["console.log()", "print()", "display"],
        resposta: "console.log()"
    },
    {
        pergunta: "Qual simbolo representa igualdade estrita?",
        opcoes: ["=", "==", "==="],
        resposta: "==="
    }
];

let perguntaAtual = 0;
let pontuacao = 0;

function mostrarPergunta() {
    const pergunta = perguntas[perguntaAtual];
    document.getElementById("pergunta").textContent = pergunta.pergunta;
    
    const opcoes = document.getElementById("opcoes");
    opcoes.innerHTML = "";
    
    pergunta.opcoes.forEach(function(opcao) {
        const botao = document.createElement("button");
        botao.textContent = opcao;
        botao.classList.add("opcao");
        
        botao.addEventListener("click", function() {
            if (opcao === pergunta.resposta) {
                pontuacao++;
            }
            document.getElementById("pontuacao").textContent = pontuacao;
            perguntaAtual++;
            
            if (perguntaAtual < perguntas.length) {
                mostrarPergunta();
            } else {
                // Erro corrigido aqui ("finalizado" com um 'i' só)
                document.getElementById("pergunta").textContent = "Quiz finalizado!";
                opcoes.innerHTML = "";
            }
        });
        
        opcoes.appendChild(botao);
    });
}

// Inicia o quiz
mostrarPergunta();