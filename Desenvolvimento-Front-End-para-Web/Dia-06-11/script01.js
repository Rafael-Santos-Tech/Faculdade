function verificar(){
    let nota = parseFloat(document.getElementById("nota").value);
    let resultado = document.getElementById("resultado");
// validação do corpo vazio ou invalido
if(isNaN(nota) || nota < 0 || nota > 10){
    resultado.textContent = "Digite uma nota valida entre 0 e 10.";
    resultado.className = "";
    return;
}
// estrutura switch
switch (true){
    case (nota >= 7):
        resultado.textContent = "Aprovado";
        resultado.className = "aprovado";
        break;
    default:
        // o default funciona como o else
        resultado.textContent = "Reprovado";
        resultado.className = "reprovado";
        break;
}
}