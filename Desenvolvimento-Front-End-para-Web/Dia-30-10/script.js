let numeros = [10,20,30,40,50];
function mostrarNumeros(){
    document.getElementById("numeros").innerHTML="Numeros: " + numeros;
}
function somarNumeros(){
    let soma = 0;
    for (let i = 0; i < numeros.length; i++){
        soma = soma + numeros[i];
    }
    document.getElementById("resultado").innerHTML="resultado da soma:" + soma;
}