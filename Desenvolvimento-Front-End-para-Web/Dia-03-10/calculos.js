function calcular(){
    let num = Number(window.prompt('Digite um número: '));
    let res = document.querySelector('section#result');
    res.innerHTML = `<p> O Número a ser analisado aqui sera o <strong>${num}</strong></p><hr>`;
    res.innerHTML += `<p> O valor absoluto é ${Math.abs(num)}</p><hr>`;
    res.innerHTML += `<p> A sua parte inteira é ${Math.trunc(num)}</p><hr>`;
    res.innerHTML += `<p> O valor inteiro mais proximo é  ${Math.round(num)}</p><hr>`;
    res.innerHTML += `<p> A sua raiz Quadrada é  ${Math.sqrt(num)}</p><hr>`;
    res.innerHTML += `<p> a sua raiz cubica é   ${Math.cbrt(num)}</p><hr>`;
    res.innerHTML += `<p> O valor de ${num}<sup>2</sup> é ${Math.pow(num,2)}</p>`;
    res.innerHTML += `<p> O valor de ${num}<sup>3</sup> é ${Math.pow(num,3)}</p>`;
    




}