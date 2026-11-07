function verificar(){
    let nota = parseFloat(document.getElementById("nota").value);
    let resultado = document.getElementById("resultado");
// estrutura if/ else
if(nota>=7){
    resultado.textContent = "Aprovado";
    resultado.className = "aprovado";
} else {
    resultado.textContent = "Reprovado";
    resultado.className = "reprovado";
}
}