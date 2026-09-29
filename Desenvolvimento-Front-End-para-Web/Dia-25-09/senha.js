document.getElementById("gerar").addEventListener("click", function() {
    const tamanho = Number(document.getElementById("tamanho").value);
    
    const caracteres = 
        "ABCDEFGHIJKLMNOPQRSTVUWXYZ" +
        "abcdefghijklmnopqrstuvwxyz" +
        "0123456789" + 
        "!#$%@&*";
        
    let senha = "";
    
    for (let i = 0; i < tamanho; i++) {
        const numeroAleatorio = Math.floor(Math.random() * caracteres.length);
        senha += caracteres[numeroAleatorio];
    }
    
    document.getElementById("senha").textContent = senha;
});