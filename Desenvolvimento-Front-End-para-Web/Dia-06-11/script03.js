
function verificar() {
    let notas = [8, 5, 9, 6, 7, 4, 10];
    let resultado = document.getElementById("resultado");

    // Limpando resultado
    resultado.innerHTML = "";

    for (let i = 0; i < notas.length; i++) {
        resultado.innerHTML += "<p>Aluno " + (i + 1) + " - Nota: " + notas[i] + "</p>";

        // Verificar aprovação
        if (notas[i] >= 7) {
            resultado.innerHTML += "<p style='color:green'>Aprovado!</p>";
        } else {
            resultado.innerHTML += "<p style='color:red'>Reprovado!</p>";
        }
    }
}
