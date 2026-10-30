function somar() {
    let n1 = parseInt(window.prompt('Digite um número: '));
    let n2 = parseInt(window.prompt('Digite outro número: '));
    
    let soma = n1 + n2;
    
    window.alert(`A soma entre ${n1} e ${n2} é igual a ${soma}!`);
}