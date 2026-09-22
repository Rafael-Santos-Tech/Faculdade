document.getElementById("calcular").addEventListener("click", function(){
    const numero1 = Number(document.getElementById("numero1").value);
    const numero2 = Number(document.getElementById("numero2").value);
    const operacao = document.getElementById("operacao").value;
    let reesultado;
    if (operacao === "soma"){
        reesultado = numero1 + numero2;
    }
    else if (operacao === "subtracao"){
        reesultado = numero1 - numero2;
    }
    else if (operacao === "mutiplicacao"){
        reesultado = numero1 * numero2;
    }
    else if (operacao === "divisao"){
        reesultado = numero1 / numero2;
    }
    document.getElementById("resultado").textContent = reesultado;
});