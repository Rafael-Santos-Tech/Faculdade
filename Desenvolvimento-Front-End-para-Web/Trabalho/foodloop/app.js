/* =====================================================================
   Loopfood — app.js
   0. Utilidades        3. Favoritos e catálogo
   1. Acessibilidade    4. Carrinho e pedidos
   2. Pular link        5. Formulários e inicialização
   ===================================================================== */
'use strict';

/* 0. UTILIDADES ------------------------------------------------------ */
const CHAVES = {
    a11y: 'loopfood:a11y',
    favoritos: 'loopfood:favoritos',
    carrinho: 'loopfood:carrinho',
    pedidos: 'loopfood:pedidos',
};
const TAXA_ENTREGA = 5;

const $ = (seletor, raiz = document) => raiz.querySelector(seletor);
const $$ = (seletor, raiz = document) => [...raiz.querySelectorAll(seletor)];
const brl = (n) => n.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });

function ler(chave, padrao) {
    try {
        return JSON.parse(localStorage.getItem(chave)) ?? padrao;
    } catch {
        return padrao;
    }
}

function salvar(chave, valor) {
    try {
        localStorage.setItem(chave, JSON.stringify(valor));
    } catch {
        /* armazenamento indisponível (modo privado, por exemplo) */
    }
}

const lerLista = (chave) => {
    const lista = ler(chave, []);
    return Array.isArray(lista) ? lista : [];
};

/* Cria elementos sem innerHTML (evita injeção de HTML a partir do localStorage). */
function el(tag, atributos = {}, ...filhos) {
    const e = document.createElement(tag);
    for (const [nome, valor] of Object.entries(atributos)) {
        if (nome === 'texto') e.textContent = valor;
        else if (valor !== false && valor != null) e.setAttribute(nome, valor);
    }
    e.append(...filhos);
    return e;
}

/* Região ao vivo: leitores de tela anunciam o que mudou na página. */
let regiaoAnuncio;
function anunciar(mensagem) {
    if (!regiaoAnuncio) return;
    regiaoAnuncio.textContent = '';
    setTimeout(() => { regiaoAnuncio.textContent = mensagem; }, 50);
}

/* 1. ACESSIBILIDADE: tema escuro e modo para daltonismo -------------- */
const raiz = document.documentElement;

function lerPreferencias() {
    const escuroNoSistema = window.matchMedia?.('(prefers-color-scheme: dark)').matches ?? false;
    return { escuro: escuroNoSistema, daltonismo: false, ...ler(CHAVES.a11y, {}) };
}

function aplicarPreferencias(prefs) {
    raiz.dataset.tema = prefs.escuro ? 'escuro' : 'claro';
    raiz.dataset.daltonismo = prefs.daltonismo ? 'true' : 'false';
}

/* Roda já no <head>, antes da primeira pintura: evita o "flash" de tema claro. */
aplicarPreferencias(lerPreferencias());

function iniciarWidgetAcessibilidade() {
    const botao = $('#botao-acessibilidade');
    const painel = $('#painel-acessibilidade');
    if (!botao || !painel) return;
    const widget = botao.closest('.widget-acessibilidade');

    const abrir = (aberto) => {
        painel.hidden = !aberto;
        botao.setAttribute('aria-expanded', String(aberto));
    };

    botao.addEventListener('click', () => abrir(painel.hidden));
    document.addEventListener('click', (e) => { if (!widget.contains(e.target)) abrir(false); });
    widget.addEventListener('focusout', (e) => {
        if (e.relatedTarget && !widget.contains(e.relatedTarget)) abrir(false);
    });
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && !painel.hidden) {
            abrir(false);
            botao.focus();
        }
    });

    const prefs = lerPreferencias();
    const ligarOpcao = (seletor, chave, aviso) => {
        const opcao = $(seletor, painel);
        if (!opcao) return;
        opcao.setAttribute('aria-pressed', String(prefs[chave]));
        opcao.addEventListener('click', () => {
            prefs[chave] = !prefs[chave];
            opcao.setAttribute('aria-pressed', String(prefs[chave]));
            aplicarPreferencias(prefs);
            salvar(CHAVES.a11y, prefs);
            anunciar(`${aviso} ${prefs[chave] ? 'ativado' : 'desativado'}`);
        });
    };
    ligarOpcao('.botao-tema', 'escuro', 'Modo escuro');
    ligarOpcao('.botao-daltonismo', 'daltonismo', 'Modo para daltonismo');
}

/* 2. PULAR LINK: leva o foco (não só a rolagem) até o conteúdo ------- */
function iniciarPularLink() {
    $$('.pular-link').forEach((link) => link.addEventListener('click', () => {
        const alvo = document.getElementById(link.hash.slice(1));
        if (!alvo) return;
        if (!alvo.hasAttribute('tabindex')) alvo.setAttribute('tabindex', '-1');
        alvo.focus();
    }));
}

/* 3. FAVORITOS ------------------------------------------------------- */
const lerFavoritos = () => lerLista(CHAVES.favoritos);

function alternarFavorito(id, nome, preco, img, botao) {
    const favoritos = lerFavoritos();
    const jaEra = favoritos.some((f) => f.id === id);
    salvar(CHAVES.favoritos, jaEra
        ? favoritos.filter((f) => f.id !== id)
        : [...favoritos, { id, nome, preco, img }]);
    if (botao) botao.setAttribute('aria-pressed', String(!jaEra));
    atualizarContadores();
    anunciar(`${nome} ${jaEra ? 'removido dos' : 'adicionado aos'} favoritos`);
    return !jaEra;
}

function sincronizarCoracoes() {
    const ids = new Set(lerFavoritos().map((f) => f.id));
    $$('.btn-fav-card').forEach((botao) => {
        const id = botao.closest('[data-id]')?.dataset.id;
        botao.setAttribute('aria-pressed', String(ids.has(id)));
    });
}

function renderFavoritos() {
    const lista = $('#lista-favoritos');
    if (!lista) return;
    const favoritos = lerFavoritos();
    lista.replaceChildren();
    lista.setAttribute('tabindex', '-1');
    if (!favoritos.length) {
        lista.append(el('p', { class: 'vazio' }, 'Você ainda não favoritou nenhum produto. ',
            el('a', { href: 'produtos.html' }, 'Ver produtos')));
        return;
    }
    favoritos.forEach((f) => lista.append(
        el('article', { class: 'card-produto', 'data-id': f.id, 'data-nome': f.nome, 'data-preco': f.preco, 'data-img': f.img },
            el('img', { src: f.img, alt: '', loading: 'lazy' }),
            el('h2', { texto: f.nome }),
            el('span', { class: 'produto-preco', texto: brl(Number(f.preco)) }),
            el('button', { type: 'button', class: 'btn-add' }, 'Adicionar ao carrinho',
                el('span', { class: 'sr-only', texto: `: ${f.nome}` })),
            el('button', { type: 'button', class: 'btn-remover btn-remover-fav' }, 'Remover dos favoritos',
                el('span', { class: 'sr-only', texto: `: ${f.nome}` })))));
}

/* 3.1 CATÁLOGO: fonte única dos produtos (cardápio completo e categorias).
   Mesma estrutura dos produtos já existentes: id, nome, descricao, preco, img. */
const CATEGORIAS = [
    { slug: 'lanches',  nome: 'Lanches',               img: 'img/burguer-loop.jpg' },
    { slug: 'pizzas',   nome: 'Pizzas',                img: 'img/frango-catupiry.jpg' },
    { slug: 'japonesa', nome: 'Comida Japonesa',       img: 'img/combo-sushi.jpg' },
    { slug: 'saudavel', nome: 'Saudável & Saladas',    img: 'img/salada-com-frango-desfiado.jpg' },
    { slug: 'doces',    nome: 'Sobremesas & Doces',    img: 'img/bolo-de-ferrero.jpg' },
    { slug: 'bebidas',  nome: 'Bebidas',               img: 'img/caldo-de-cana.jpg' },
];

const PRODUTOS = [
    { id: 'p1', cat: 'lanches', nome: 'Burguer Loop', preco: 28.90, img: 'img/burguer-loop.jpg',
      descricao: 'Pão artesanal, hamburguer artesanal 180g, queijo cheddar e molho especial.' },
    { id: 'p7', cat: 'lanches', nome: 'X-Bacon Artesanal', preco: 32.90, img: 'img/x-bacon-artesanal.jpg',
      descricao: 'Pão brioche, hambúrguer de 160g, fatias de bacon crocante, queijo prato e maionese da casa.' },
    { id: 'p8', cat: 'lanches', nome: 'Cheeseburger Duplo', preco: 36.90, img: 'img/cheeseburguer-duplo.jpg',
      descricao: 'Pão brioche, dois hambúrgueres de 120g, queijo cheddar derretido, picles e molho especial.' },

    { id: 'p3', cat: 'pizzas', nome: 'Pizza Frango c/ Catupiry', preco: 45.00, img: 'img/frango-catupiry.jpg',
      descricao: 'Massa artesanal, bastante frango desfiado e catupiry original.' },
    { id: 'p9', cat: 'pizzas', nome: 'Pizza Calabresa', preco: 42.90, img: 'img/pizza-calabresa.jpg',
      descricao: 'Molho de tomate, queijo muçarela, calabresa fatiada, cebola e azeitonas.' },
    { id: 'p10', cat: 'pizzas', nome: 'Pizza Quatro Queijos', preco: 52.90, img: 'img/pizza-quatro-queijos.jpg',
      descricao: 'Muçarela, provolone, parmesão e catupiry sobre massa artesanal.' },

    { id: 'p2', cat: 'japonesa', nome: 'Combo Sushi Especial', preco: 59.90, img: 'img/combo-sushi.jpg',
      descricao: 'Combo com 20 peças variadas entre hots, uramakis e niguiris.' },
    { id: 'p11', cat: 'japonesa', nome: 'Temaki de Salmão', preco: 29.90, img: 'img/temaki-de-salmao.jpg',
      descricao: 'Cone de alga nori com arroz, salmão fresco e cream cheese.' },
    { id: 'p12', cat: 'japonesa', nome: 'Yakisoba de Frango', preco: 36.90, img: 'img/yakisoba-de-frango.jpg',
      descricao: 'Macarrão oriental salteado com frango, legumes frescos e molho shoyu.' },

    { id: 'p5', cat: 'saudavel', nome: 'Salada c/ Frango Desfiado', preco: 22.00, img: 'img/salada-com-frango-desfiado.jpg',
      descricao: 'Mix de folhas verdes, tomate cereja, cenoura e frango grelhado.' },
    { id: 'p13', cat: 'saudavel', nome: 'Salada Caesar com Frango', preco: 26.90, img: 'img/salada-caesar-com-frango.jpg',
      descricao: 'Alface americana, frango grelhado, lascas de parmesão, croutons e molho caesar.' },
    { id: 'p14', cat: 'saudavel', nome: 'Bowl Fit de Frango', preco: 29.90, img: 'img/bowl-fit-de-frango.jpg',
      descricao: 'Arroz integral, frango grelhado, batata-doce assada, brócolis e cenoura.' },

    { id: 'p4', cat: 'doces', nome: 'Bolo de Ferrero Rocher', preco: 18.50, img: 'img/bolo-de-ferrero.jpg',
      descricao: 'Fatia generosa com recheio cremoso de avelã e avelãs picadas.' },
    { id: 'p15', cat: 'doces', nome: 'Brownie com Sorvete', preco: 19.90, img: 'img/brownie-com-sorvete.jpg',
      descricao: 'Brownie de chocolate quentinho com uma bola de sorvete de creme e calda de chocolate.' },
    { id: 'p16', cat: 'doces', nome: 'Açaí 500ml', preco: 24.90, img: 'img/acai-500ml.jpg',
      descricao: 'Açaí cremoso com banana, granola e leite em pó.' },

    { id: 'p6', cat: 'bebidas', nome: 'Caldo de Cana 500ml', preco: 8.00, img: 'img/caldo-de-cana.jpg',
      descricao: 'Caldo de cana gelado e moído na hora.' },
    { id: 'p17', cat: 'bebidas', nome: 'Suco de Laranja Natural 500ml', preco: 10.90, img: 'img/suco-de-laranja-natural-500ml.jpg',
      descricao: 'Suco de laranja espremido na hora, sem adição de açúcar.' },
    { id: 'p18', cat: 'bebidas', nome: 'Refrigerante Lata 350ml', preco: 6.50, img: 'img/refrigerante-lata-350ml.jpg',
      descricao: 'Refrigerante gelado, lata de 350ml.' },
];

const ICONE_CORACAO = '<svg aria-hidden="true" focusable="false" viewBox="0 0 24 24"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>';

/* Mesmo cartão do cardápio: favoritar, imagem, nome, descrição, preço e botão. */
function criarCardProduto(p) {
    const botaoFav = el('button', {
        type: 'button', class: 'btn-fav-card', 'aria-pressed': 'false', 'aria-label': `Favoritar ${p.nome}`,
    });
    botaoFav.innerHTML = ICONE_CORACAO; /* constante do código, sem dados de usuário */
    return el('article', { class: 'card-produto', 'data-id': p.id, 'data-nome': p.nome, 'data-preco': p.preco.toFixed(2), 'data-img': p.img },
        botaoFav,
        el('img', { src: p.img, alt: '', loading: 'lazy' }),
        el('h2', { texto: p.nome }),
        el('p', { class: 'descricao', texto: p.descricao }),
        el('span', { class: 'produto-preco', texto: brl(p.preco) }),
        el('button', { type: 'button', class: 'btn-add' }, 'Adicionar ao carrinho',
            el('span', { class: 'sr-only', texto: `: ${p.nome}` })));
}

function renderCardapio() {
    const lista = $('#lista-produtos');
    if (!lista) return;
    lista.replaceChildren(...PRODUTOS.map(criarCardProduto));
}

/* Categorias: ?cat=slug mostra todos os produtos da categoria escolhida. */
function renderCategoria() {
    const secao = $('#produtos-categoria');
    if (!secao) return;
    const slug = new URLSearchParams(window.location.search).get('cat');
    const categoria = CATEGORIAS.find((c) => c.slug === slug);

    $$('.categoria-card a').forEach((a) => {
        if (new URL(a.href).searchParams.get('cat') === slug) a.setAttribute('aria-current', 'true');
        else a.removeAttribute('aria-current');
    });
    if (!categoria) { secao.hidden = true; return; }

    const produtos = PRODUTOS.filter((p) => p.cat === categoria.slug);
    $('#titulo-produtos-categoria').textContent = categoria.nome;
    $('#lista-categoria').replaceChildren(...produtos.map(criarCardProduto));
    secao.hidden = false;
    document.title = `Loopfood - ${categoria.nome}`;

    /* Leva a rolagem e o foco (teclado e leitor de tela) até os produtos. */
    const titulo = $('#titulo-produtos-categoria');
    titulo.focus({ preventScroll: true });
    secao.scrollIntoView({ block: 'start' });
    anunciar(`${categoria.nome}: ${produtos.length} produtos`);
}

/* 4. CARRINHO E PEDIDOS ---------------------------------------------- */
const lerCarrinho = () => lerLista(CHAVES.carrinho);
const calcularSubtotal = (itens) => itens.reduce((soma, i) => soma + i.preco * i.qtd, 0);

function adicionarAoCarrinho(id, nome, preco, img) {
    const itens = lerCarrinho();
    const existente = itens.find((i) => i.id === id);
    if (existente) existente.qtd += 1;
    else itens.push({ id, nome, preco, img, qtd: 1 });
    salvar(CHAVES.carrinho, itens);
    atualizarContadores();
    anunciar(`${nome} adicionado ao carrinho`);
}

function alterarQuantidade(id, delta) {
    const itens = lerCarrinho();
    const item = itens.find((i) => i.id === id);
    if (!item) return;
    item.qtd = Math.max(1, item.qtd + delta);
    salvar(CHAVES.carrinho, itens);
    renderCarrinho();
    atualizarContadores();
    $(`[data-id="${CSS.escape(id)}"] [data-acao="${delta > 0 ? 'mais' : 'menos'}"]`)?.focus();
    anunciar(`${item.nome}: ${item.qtd} ${item.qtd === 1 ? 'unidade' : 'unidades'}`);
}

function removerDoCarrinho(id) {
    const itens = lerCarrinho();
    const item = itens.find((i) => i.id === id);
    salvar(CHAVES.carrinho, itens.filter((i) => i.id !== id));
    renderCarrinho();
    atualizarContadores();
    $('#lista-carrinho')?.focus();
    anunciar(`${item?.nome ?? 'Item'} removido do carrinho`);
}

function renderCarrinho() {
    const lista = $('#lista-carrinho');
    if (!lista) return;
    const itens = lerCarrinho();
    lista.replaceChildren();
    lista.setAttribute('tabindex', '-1');

    if (!itens.length) {
        lista.append(el('p', { class: 'vazio' }, 'Seu carrinho está vazio. ',
            el('a', { href: 'produtos.html' }, 'Ver produtos')));
    }
    itens.forEach((i) => lista.append(
        el('article', { class: 'item-carrinho', 'data-id': i.id },
            el('img', { src: i.img, alt: '' }),
            el('div', { class: 'item-info' },
                el('h2', { texto: i.nome }),
                el('span', { class: 'produto-preco', texto: brl(i.preco) })),
            el('div', { class: 'qtd', role: 'group', 'aria-label': `Quantidade de ${i.nome}` },
                el('button', {
                    type: 'button', 'data-acao': 'menos',
                    'aria-label': `Diminuir quantidade de ${i.nome}`,
                    'aria-disabled': i.qtd <= 1 ? 'true' : null,
                }, '−'),
                el('span', { class: 'qtd-valor', texto: i.qtd }),
                el('button', { type: 'button', 'data-acao': 'mais', 'aria-label': `Aumentar quantidade de ${i.nome}` }, '+')),
            el('button', { type: 'button', class: 'btn-remover', 'data-acao': 'remover' }, 'Remover',
                el('span', { class: 'sr-only', texto: `: ${i.nome}` })))));

    const subtotal = calcularSubtotal(itens);
    const taxa = itens.length ? TAXA_ENTREGA : 0;
    const escrever = (id, valor) => { const alvo = $(id); if (alvo) alvo.textContent = brl(valor); };
    escrever('#subtotal-carrinho', subtotal);
    escrever('#taxa-carrinho', taxa);
    escrever('#total-carrinho', subtotal + taxa);
}

function finalizarPedido() {
    const itens = lerCarrinho();
    if (!itens.length) {
        anunciar('Seu carrinho está vazio. Adicione produtos para finalizar o pedido.');
        return;
    }
    const pedidos = lerLista(CHAVES.pedidos);
    const subtotal = calcularSubtotal(itens);
    const pedido = {
        numero: (pedidos.at(-1)?.numero ?? 1000) + 1,
        data: new Date().toISOString(),
        itens,
        subtotal,
        taxa: TAXA_ENTREGA,
        total: subtotal + TAXA_ENTREGA,
        status: 'Em preparo',
    };
    salvar(CHAVES.pedidos, [...pedidos, pedido]);
    salvar(CHAVES.carrinho, []);
    renderCarrinho();
    atualizarContadores();

    const confirmacao = el('div', { class: 'confirmacao', tabindex: '-1' },
        el('h2', { texto: `Pedido #${pedido.numero} realizado!` }),
        el('p', {}, 'Acompanhe o andamento em ', el('a', { href: 'pedidos.html' }, 'Meus pedidos'), '.'));
    $('#lista-carrinho').replaceChildren(confirmacao);
    confirmacao.focus();
}

function renderPedidos() {
    const lista = $('#lista-pedidos');
    if (!lista) return;
    const pedidos = lerLista(CHAVES.pedidos).reverse();
    if (!pedidos.length) {
        lista.append(el('p', { class: 'vazio' }, 'Você ainda não fez nenhum pedido. ',
            el('a', { href: 'produtos.html' }, 'Ver produtos')));
        return;
    }
    pedidos.forEach((p) => lista.append(
        el('article', { class: 'pedido' },
            el('h2', { texto: `Pedido #${p.numero}` }),
            el('p', { texto: `Feito em ${new Date(p.data).toLocaleString('pt-BR', { dateStyle: 'short', timeStyle: 'short' })}. Status: ${p.status}.` }),
            el('ul', {}, ...p.itens.map((i) => el('li', { texto: `${i.qtd}× ${i.nome}: ${brl(i.preco * i.qtd)}` }))),
            el('p', { class: 'pedido-total', texto: `Total: ${brl(p.total)} (entrega de ${brl(p.taxa)} inclusa)` }))));
}

function atualizarContadores() {
    const totalFavoritos = lerFavoritos().length;
    const totalCarrinho = lerCarrinho().reduce((soma, i) => soma + i.qtd, 0);
    $$('.badge-favoritos').forEach((b) => { b.textContent = totalFavoritos; });
    $$('.badge-carrinho').forEach((b) => { b.textContent = totalCarrinho; });
}

/* 5. FORMULÁRIOS E INICIALIZAÇÃO ------------------------------------- */
function iniciarFormularios() {
    /* O "submit" só dispara se a validação nativa passar. Interceptamos para
       que usuário e senha nunca apareçam na URL (o formulário era method GET). */
    $$('form.form-auth').forEach((form) => form.addEventListener('submit', (e) => {
        e.preventDefault();
        window.location.href = 'home.html';
    }));
}

function iniciarCliques() {
    /* Botões dos cards de produto (produtos e favoritos). */
    document.addEventListener('click', (e) => {
        const botao = e.target.closest('button');
        const card = botao?.closest('[data-id][data-nome]');
        if (!card) return;
        const { id, nome, img } = card.dataset;
        const preco = Number(card.dataset.preco);
        if (botao.matches('.btn-fav-card')) alternarFavorito(id, nome, preco, img, botao);
        else if (botao.matches('.btn-add')) adicionarAoCarrinho(id, nome, preco, img);
        else if (botao.matches('.btn-remover-fav')) {
            alternarFavorito(id, nome, preco, img);
            renderFavoritos();
            $('#lista-favoritos')?.focus();
        }
    });

    /* Botões das linhas do carrinho. */
    $('#lista-carrinho')?.addEventListener('click', (e) => {
        const botao = e.target.closest('button[data-acao]');
        if (!botao) return;
        const id = botao.closest('[data-id]').dataset.id;
        if (botao.dataset.acao === 'remover') removerDoCarrinho(id);
        else alterarQuantidade(id, botao.dataset.acao === 'mais' ? 1 : -1);
    });

    $('#btn-finalizar-compra')?.addEventListener('click', finalizarPedido);
}

function iniciar() {
    regiaoAnuncio = el('div', { class: 'sr-only', role: 'status', 'aria-live': 'polite' });
    document.body.append(regiaoAnuncio);

    iniciarWidgetAcessibilidade();
    iniciarPularLink();
    iniciarFormularios();
    iniciarCliques();

    renderCardapio();
    renderCategoria();
    sincronizarCoracoes();
    renderFavoritos();
    renderCarrinho();
    renderPedidos();
    atualizarContadores();
}

if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', iniciar);
else iniciar();

/* Compatibilidade com chamadas diretas (onclick) em outras páginas. */
Object.assign(window, { alternarFavorito, adicionarAoCarrinho });
