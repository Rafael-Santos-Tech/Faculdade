function media(){
    let nom = window.prompt('Qual o nome do aluno? '); 
    let n1 = Number(window.prompt('Digite a primeira nota: '));
    let n2 = Number(window.prompt('Digite a segunda nota: '));
    let media = (n1 + n2) /2;
    let situacao = document.querySelector('section#situacao');
    situacao.innerHTML = `<p>Calculando a media final de <mark>${nom}</mark>.</p>
                        <p>As notas obtidas foram <mark>${n1} e ${n2} </mark>.</p>
                        <p>a media final sera <mark>${media}</mark>.</p>`;


}