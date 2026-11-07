function verificar(){
    let nota = parseFloat(document.getElementById("nota").value);
    let resultado = document.getElementById("resultado");
// verificar se a nota foi preenchida
if(isNaN(nota) || nota < 0 || nota > 10){
    resultado.textContent = "Digite uma nota valida entre 0 e 10!";
    resultado.style.color = "orange";
    return;
}
// estrutura de repetiacao while
let contador = 0;
while (contador < 1){
    if (nota >= 7){
        resultado.textContent = "Aprovado! Parabéns!";
        resultado.style.color = "green";
    } else {
        resultado.textContent = "Reprovado! Estude mais inutil!";
        resultado.style.color = "red";
    }
    
    contador++;
}
}