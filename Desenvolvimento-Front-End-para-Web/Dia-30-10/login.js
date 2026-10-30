// Captura o formulário pelo ID
const formulario = document.getElementById('formLogin');

// Adiciona o evento de 'submit' ao formulário
formulario.addEventListener('submit', function(event) {
    // Impede que a página recarregue ao enviar o formulário
    event.preventDefault();

    // Captura os elementos de input e as tags span de erro
    const emailInput = document.getElementById('email');
    const senhaInput = document.getElementById('senha');
    const erroEmail = document.getElementById('erroEmail');
    const erroSenha = document.getElementById('erroSenha');

    // Limpa as mensagens e cores de erro anteriores antes de validar novamente
    emailInput.classList.remove('input-erro');
    erroEmail.style.display = 'none';
    erroEmail.innerText = '';

    senhaInput.classList.remove('input-erro');
    erroSenha.style.display = 'none';
    erroSenha.innerText = '';

    let formularioValido = true;

    // Validação do campo e-mail
    if (emailInput.value.trim() === "") {
        emailInput.classList.add('input-erro');
        erroEmail.innerText = "O campo e-mail deve ser preenchido.";
        erroEmail.style.display = 'block';
        formularioValido = false;
    }

    // Validação do campo senha
    if (senhaInput.value.trim() === "") {
        senhaInput.classList.add('input-erro');
        erroSenha.innerText = "O campo senha deve ser preenchido.";
        erroSenha.style.display = 'block';
        formularioValido = false;
    }

    // Se tudo estiver preenchido corretamente
    if (formularioValido) {
        window.alert("Validação concluída com sucesso! Os dados podem ser enviados.");
        // Aqui você enviaria os dados para um servidor (backend)
    }
});