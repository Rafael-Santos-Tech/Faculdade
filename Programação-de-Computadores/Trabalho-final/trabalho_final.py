#Loja online de jogos
"""
Bibliotecas
"""
import json
import csv
import datetime
import random
from math import floor

ARQUIVO_CATALOGO = "catalogo.json"
ARQUIVO_USUARIOS = "usuarios.json"
ARQUIVO_PEDIDOS = "pedidos.json"
"""
biblioteca com os Jogos, Valores, Gêneros e Avaliações.
"""
CATALOGO_INICIAL: list[dict] = [
    #--------Aventura-------
    {"id": 1, "titulo": "Minecraft", "genero": "Aventura", "preco": 99.90, "avaliacao": 4.9},
    {"id": 2, "titulo": "Hollow Knight", "genero": "Aventura", "preco": 39.99, "avaliacao": 4.9},
    {"id": 3, "titulo": "Fortnite", "genero": "Aventura", "preco": 00.00, "avaliacao": 4.7},
    {"id": 4, "titulo": "Ori and the Will of the Wisps", "genero": "Aventura", "preco": 49.99, "avaliacao": 4.9},
    {"id": 5, "titulo": "A Short Hike", "genero": "Aventura", "preco": 15.99, "avaliacao": 4.9},
    {"id": 6, "titulo": "Firewatch", "genero": "Aventura", "preco": 24.99, "avaliacao": 4.7},
    {"id": 7, "titulo": "Disco Elysium","genero": "Aventura", "preco": 59.99, "avaliacao": 4.8},
    {"id": 8, "titulo": "What Remains of Edith Finch", "genero": "Aventura", "preco": 24.99, "avaliacao": 4.9},
    {"id": 9, "titulo": "Subnautica",  "genero": "Aventura", "preco": 49.99, "avaliacao": 4.8},
    {"id": 10, "titulo": "The Stanley Parable Ultra Deluxe", "genero": "Aventura", "preco": 39.99, "avaliacao": 4.9},
    {"id": 11, "titulo": "Clair Obscur: Expedition 33", "genero": "Aventura", "preco": 199.99, "avaliacao": 4.9},
    {"id": 12, "titulo": "Hollow Knight:Silksong",  "genero": "Aventura", "preco": 67.99, "avaliacao": 4.8},
    {"id": 13, "titulo": "It Takes Two", "genero": "Aventura", "preco": 99.90, "avaliacao": 4.9},
    {"id": 14, "titulo": "Red Dead Redemption 2", "genero": "Aventura", "preco": 187.95, "avaliacao": 4.9},
    {"id": 15, "titulo": "God of War", "genero": "Aventura", "preco": 119.99, "avaliacao": 4.9},
    {"id": 16, "titulo": "Devil May Cry 5", "genero": "Aventura", "preco": 129.99, "avaliacao": 4.8},
    {"id": 17, "titulo": "Sekiro: Shadows Die Twice", "genero": "Aventura", "preco": 199.99, "avaliacao": 4.8},
    {"id": 18, "titulo": "Doom Eternal", "genero": "Aventura", "preco": 69.99, "avaliacao": 4.7},
    {"id": 19, "titulo": "Control Ultimate Edition", "genero": "Aventura", "preco": 59.99, "avaliacao": 4.7},
    {"id": 20, "titulo": "Monster Hunter: World", "genero": "Aventura", "preco": 59.99, "avaliacao": 4.8},
    {"id": 21, "titulo": "Ghostwire: Tokyo", "genero": "Aventura", "preco": 99.99, "avaliacao": 4.3},
    {"id": 22, "titulo": "Monster Hunter Wilds", "genero": "Aventura", "preco": 299.99, "avaliacao": 4.7},
    {"id": 23, "titulo": "Dave the Diver", "genero": "Aventura", "preco": 49.99, "avaliacao": 4.8},
    {"id": 24, "titulo": "Portal 2", "genero": "Aventura", "preco": 29.99, "avaliacao": 4.9},
    {"id": 25,"titulo": "Return of the Obra Dinn", "genero": "Aventura", "preco": 34.99, "avaliacao": 4.9},
    {"id": 26, "titulo": "The Witness", "genero": "Aventura", "preco": 49.99, "avaliacao": 4.5},
    {"id": 27, "titulo": "Antichamber", "genero": "Aventura", "preco": 19.99, "avaliacao": 4.6},
    {"id": 28, "titulo": "Manifold Garden", "genero": "Aventura", "preco": 24.99, "avaliacao": 4.6},
    {"id": 29, "titulo": "Superhot", "genero": "Aventura", "preco": 34.99, "avaliacao": 4.7},
    {"id": 30, "titulo": "The Witcher 3: Wild Hunt", "genero": "Aventura", "preco": 99.99, "avaliacao": 4.9},
    {"id": 31, "titulo": "Baldur's Gate 3", "genero": "Aventura", "preco": 199.90, "avaliacao": 5.0},
    {"id": 32, "titulo": "Mass Effect Legendary Edition", "genero": "Aventura", "preco": 99.99, "avaliacao": 4.8},
    {"id": 33, "titulo": "Dragon Age: Origins", "genero": "Aventura", "preco": 19.99, "avaliacao": 4.8},
    {"id": 34, "titulo": "Dark Souls III", "genero": "Aventura", "preco": 99.99, "avaliacao": 4.8},
    {"id": 35, "titulo": "Pathfinder: Wrath of Righteous", "genero": "Aventura", "preco": 79.99, "avaliacao": 4.7},
    {"id": 36, "titulo": "Kingdom Come: Deliverance 2", "genero": "Aventura", "preco": 249.90, "avaliacao": 4.8},
    #--------Esporte------
    {"id": 37, "titulo": "FIFA 25", "genero": "Esporte", "preco": 299.90, "avaliacao": 4.1},
    {"id": 38, "titulo": "EA Sports FC 26", "genero": "Esporte", "preco": 299.99, "avaliacao": 4.1},
    {"id": 39, "titulo": "NBA 2K25", "genero": "Esporte", "preco": 249.99, "avaliacao": 3.9},
    {"id": 40, "titulo": "MLB The Show 25", "genero": "Esporte", "preco": 249.99, "avaliacao": 4.3},
    {"id": 41, "titulo": "Tony Hawk's Pro Skater 1+2", "genero": "Esporte", "preco": 79.99, "avaliacao": 4.8},
    {"id": 42, "titulo": "Steep", "genero": "Esporte", "preco": 49.99, "avaliacao": 4.3},
    {"id": 43, "titulo": "Rocket League", "genero": "Esporte", "preco": 0.00, "avaliacao": 4.6},
    #--------Ação-------
    {"id": 44, "titulo": "Hollow Knight:Silksong", "genero": "Ação", "preco": 67.99, "avaliacao": 4.8},
    {"id": 45, "titulo": "Red Dead Redemption 2", "genero": "Ação", "preco": 187.95, "avaliacao": 4.9},
    {"id": 46, "titulo": "God of War", "genero": "Ação", "preco": 119.99, "avaliacao": 4.9},
    {"id": 47, "titulo": "Devil May Cry 5", "genero": "Ação", "preco": 129.99, "avaliacao": 4.8},
    {"id": 48, "titulo": "Sekiro: Shadows Die Twice", "genero": "Ação", "preco": 199.99, "avaliacao": 4.8},
    {"id": 49, "titulo": "Doom Eternal", "genero": "Ação", "preco": 69.99, "avaliacao": 4.7},
    {"id": 50, "titulo": "Hades", "genero": "Ação", "preco": 37.99, "avaliacao": 4.9},
    {"id": 51, "titulo": "Control Ultimate Edition", "genero": "Ação", "preco": 59.99, "avaliacao": 4.7},
    {"id": 52, "titulo": "Monster Hunter: World", "genero": "Ação", "preco": 59.99, "avaliacao": 4.8},
    {"id": 53, "titulo": "Ghostwire: Tokyo", "genero": "Ação", "preco": 99.99, "avaliacao": 4.3},
    {"id": 54, "titulo": "Monster Hunter Wilds", "genero": "Ação", "preco": 299.99, "avaliacao": 4.7},
    {"id": 55, "titulo": "Hollow Knight", "genero": "Ação", "preco": 39.99, "avaliacao": 4.9},
    {"id": 56, "titulo": "Ori and the Will of the Wisps", "genero": "Ação", "preco": 49.99, "avaliacao": 4.9},
    {"id": 57, "titulo": "Subnautica", "genero": "Ação", "preco": 49.99, "avaliacao": 4.8},
    {"id": 58, "titulo": "Clair Obscur: Expedition 33", "genero": "Ação", "preco": 199.99, "avaliacao": 4.9},
    {"id": 59, "titulo": "Steep", "genero": "Ação", "preco": 49.99, "avaliacao": 4.3},
    {"id": 60, "titulo": "Among Us", "genero": "Ação", "preco":  9.99, "avaliacao": 4.5},
    {"id": 61, "titulo": "Untitled Goose Game", "genero": "Ação", "preco": 29.99, "avaliacao": 4.7},
    {"id": 62, "titulo": "Overcooked! 2", "genero": "Ação", "preco": 49.99, "avaliacao": 4.6},
    {"id": 63, "titulo": "Dave the Diver", "genero": "Ação", "preco": 49.99, "avaliacao": 4.8},
    {"id": 64, "titulo": "Vampire Survivors", "genero": "Ação", "preco":  9.99, "avaliacao": 4.9},
    {"id": 65, "titulo": "Cuphead", "genero": "Ação", "preco": 49.99, "avaliacao": 4.8},
    {"id": 66, "titulo": "The Talos Principle 2", "genero": "Ação", "preco": 99.99, "avaliacao": 4.8},
    {"id": 67, "titulo": "Portal 2", "genero": "Ação", "preco": 29.99, "avaliacao": 4.9},
    {"id": 68, "titulo": "Superhot", "genero": "Ação", "preco": 34.99, "avaliacao": 4.7},
    {"id": 69, "titulo": "The Witcher 3: Wild Hunt", "genero": "Ação", "preco": 99.99, "avaliacao": 4.9},
    {"id": 70, "titulo": "Elden Ring", "genero": "Ação", "preco": 249.90, "avaliacao": 4.9},
    {"id": 71, "titulo": "Dark Souls III", "genero": "Ação", "preco": 99.99, "avaliacao": 4.8},
    {"id": 72, "titulo": "Pathfinder: Wrath of Righteous", "genero": "Ação", "preco": 79.99, "avaliacao": 4.7},
    {"id": 73, "titulo": "Kingdom Come: Deliverance 2", "genero": "Ação", "preco": 249.90, "avaliacao": 4.8},
    {"id": 74, "titulo": "Titan Fall 2", "genero": "Ação", "preco": 99.99, "avaliacao": 4.7},
    #---------Casual----------
    {"id": 75, "titulo": "Stardew Valley", "genero": "Casual", "preco": 37.99, "avaliacao": 4.9},
    {"id": 76, "titulo": "Firewatch", "genero": "Casual", "preco": 24.99, "avaliacao": 4.7},
    {"id": 77, "titulo": "The Stanley Parable Ultra Deluxe", "genero": "Casual", "preco": 39.99, "avaliacao": 4.9},
    {"id": 78, "titulo": "Among Us", "genero": "Casual", "preco":  9.99, "avaliacao": 4.5},
    {"id": 79, "titulo": "Untitled Goose Game", "genero": "Casual", "preco": 29.99, "avaliacao": 4.7},
    {"id": 80, "titulo": "Overcooked! 2", "genero": "Casual", "preco": 49.99, "avaliacao": 4.6},
    {"id": 81, "titulo": "Fall Guys", "genero": "Casual", "preco":  0.00, "avaliacao": 4.3},
    {"id": 82, "titulo": "Unpacking", "genero": "Casual", "preco": 29.99, "avaliacao": 4.8},
    {"id": 83, "titulo": "Dave the Diver", "genero": "Casual", "preco": 49.99, "avaliacao": 4.8},
    {"id": 84, "titulo": "Vampire Survivors", "genero": "Casual", "preco":  9.99, "avaliacao": 4.9},
    {"id": 85, "titulo": "Baba Is You", "genero": "Casual", "preco": 29.99, "avaliacao": 4.9},
    {"id": 86, "titulo": "The Witness", "genero": "Casual", "preco": 49.99, "avaliacao": 4.5},
    {"id": 87, "titulo": "Superhot", "genero": "Casual", "preco": 34.99, "avaliacao": 4.7},
    {"id": 88, "titulo": "F1 24", "genero": "Casual", "preco": 249.99, "avaliacao": 4.2},
    #-------------Puzzle----------
    {"id": 89, "titulo": "Portal 2", "genero": "Puzzle", "preco": 29.99, "avaliacao": 4.9},
    {"id": 90, "titulo": "The Talos Principle 2", "genero": "Puzzle", "preco": 99.99, "avaliacao": 4.8},
    {"id": 91, "titulo": "Baba Is You", "genero": "Puzzle", "preco": 29.99, "avaliacao": 4.9},
    {"id": 92, "titulo": "Return of the Obra Dinn", "genero": "Puzzle", "preco": 34.99, "avaliacao": 4.9},
    {"id": 93, "titulo": "The Witness", "genero": "Puzzle", "preco": 49.99, "avaliacao": 4.5},
    {"id": 94, "titulo": "Antichamber", "genero": "Puzzle", "preco": 19.99, "avaliacao": 4.6},
    {"id": 95, "titulo": "Manifold Garden", "genero": "Puzzle", "preco": 24.99, "avaliacao": 4.6},
    {"id": 96, "titulo": "Superhot", "genero": "Puzzle", "preco": 34.99, "avaliacao": 4.7},
    #-------------RPG-------------
    {"id": 97, "titulo": "Cyberpunk 2077", "genero": "RPG", "preco": 199.90, "avaliacao": 4.5},
    {"id": 98, "titulo": "Disco Elysium", "genero": "RPG", "preco": 59.99, "avaliacao": 4.8},
    {"id": 99, "titulo": "Clair Obscur: Expedition 33", "genero": "RPG", "preco": 199.99, "avaliacao": 4.9},
    {"id": 100, "titulo": "Sekiro: Shadows Die Twice", "genero": "RPG", "preco": 199.99, "avaliacao": 4.8},
    {"id": 101, "titulo": "Hades", "genero": "RPG", "preco": 37.99, "avaliacao": 4.9},
    {"id": 102, "titulo": "Monster Hunter: World", "genero": "RPG", "preco": 59.99, "avaliacao": 4.8},
    {"id": 103, "titulo": "Monster Hunter Wilds", "genero": "RPG", "preco": 299.99, "avaliacao": 4.7},
    {"id": 104, "titulo": "Stardew Valley", "genero": "RPG", "preco": 37.99, "avaliacao": 4.9},
    {"id": 105, "titulo": "Dave the Diver", "genero": "RPG", "preco": 49.99, "avaliacao": 4.8},
    {"id": 106, "titulo": "Vampire Survivors", "genero": "RPG", "preco": 9.99, "avaliacao": 4.9},
    {"id": 107, "titulo": "The Witcher 3: Wild Hunt", "genero": "RPG", "preco": 99.99, "avaliacao": 4.9},
    {"id": 108, "titulo": "Baldur's Gate 3", "genero": "RPG", "preco": 199.90, "avaliacao": 5.0},
    {"id": 109, "titulo": "Elden Ring", "genero": "RPG", "preco": 249.90, "avaliacao": 4.9},
    {"id": 110, "titulo": "Mass Effect Legendary Edition", "genero": "RPG", "preco": 99.99,"avaliacao": 4.8},
    {"id": 111, "titulo": "Divinity: Original Sin 2", "genero": "RPG", "preco": 59.99, "avaliacao": 4.9},
    {"id": 112, "titulo": "Dragon Age: Origins", "genero": "RPG", "preco": 19.99, "avaliacao": 4.8},
    {"id": 113, "titulo": "Dark Souls III", "genero": "RPG", "preco": 99.99, "avaliacao": 4.8},
    {"id": 114, "titulo": "Pathfinder: Wrath of Righteous", "genero": "RPG", "preco": 79.99, "avaliacao": 4.7},
    {"id": 115, "titulo": "Kingdom Come: Deliverance 2", "genero": "RPG", "preco": 249.90, "avaliacao": 4.8},
    #-------------Corrida---------
    {"id": 116, "titulo": "Rocket League", "genero": "Corrida", "preco": 0.00, "avaliacao": 4.6},
    {"id": 117, "titulo": "Forza Horizon 5", "genero": "Corrida", "preco": 199.99, "avaliacao": 4.8},
    {"id": 118, "titulo": "F1 24", "genero": "Corrida", "preco": 249.99, "avaliacao": 4.2},
    {"id": 119, "titulo": "Assetto Corsa", "genero": "Corrida", "preco": 34.99, "avaliacao": 4.7},
    {"id": 120, "titulo": "Need for Speed: Heat", "genero": "Corrida", "preco": 59.99, "avaliacao": 4.3},
    {"id": 121, "titulo": "Wreckfest", "genero": "Corrida", "preco": 79.99, "avaliacao": 4.8},
    {"id": 122, "titulo": "Hot Wheels Unleashed 2", "genero": "Corrida", "preco": 149.99, "avaliacao": 4.4},
    {"id": 123, "titulo": "Dirt Rally 2.0", "genero": "Corrida", "preco": 39.99, "avaliacao": 4.6},
    {"id": 124, "titulo": "Crash Team Racing Nitro-Fueled", "genero": "Corrida", "preco": 99.99, "avaliacao": 4.7},
    {"id": 125, "titulo": "Trackmania", "genero": "Corrida", "preco":  0.00, "avaliacao": 4.6},
]

"""
Salvar e carregar dados de um arquivo json de forma legível e se não existir retorna o valor padrão informado.
"""
def carregar_json (arquivo: str, padrao) -> any:
    try:
        with open (arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return padrao
def salvar_json(arquivo: str, dados: any) -> None:
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

"""
Apresentação de catálogo e filtragem por gênero.
"""

def exibir_catalogo (catalogo: list[dict], filtro_genero: str = "") -> None:
    print ("\n" + "~" * 70)
    print (" CATALOGO DE JOGOS ")
    print ("~" * 70)
    print (f" {'ID':<4} {'Título':<32} {'Gênero':<12} {'Preço':>8} {'Avaliação':>8}")
    print ("~" * 70)

    jogos_exibidos: int = 0 

    for jogo in catalogo:
        if filtro_genero and jogo["genero"].lower() != filtro_genero.lower():
            continue
        print (f" {jogo['id']:<4} {jogo['titulo']:<32} {jogo['genero']:<12} R${jogo['preco']:>7.2f} {jogo['avaliacao']:>8.1f}")
        jogos_exibidos += 1

    if jogos_exibidos == 0:
        print (" Nenhum jogo encontrado para este filtro. ")
    print ("~" * 70)

"""
Buscar jogo no catálogo pelo ID.
"""

def buscar_jogo_por_id (catalogo: list[dict], jogo_id: int) -> dict | None:
    for jogo in catalogo:
        if jogo["id"] == jogo_id:
            return jogo
    return None

"""
Recomenda um jogo aleatório com avaliação igual ou maior que 4.5 de avaliação, usando a biblioteca random
"""

def recomendar_jogo (catalogo: list[dict]) -> dict:
    destaques = [j for j in catalogo if j["avaliacao"] >= 4.5]
    return random.choice(destaques) if destaques else catalogo[0]

"""
Realizar cadastro de um novo usuário.
"""

def cadastro_usuario (usuarios: dict) -> tuple[str, dict]:
    print ("\n~~~~ CADASTRO DE USUÁRIO ~~~~")
    while True:
        login = input (" Escolha um login: ").strip().lower()
        if not login:
            print (" Login não pode ser vazio. ")
        elif login in usuarios:
            print (" Login já existe. Escolha outro.")
        else:
            break

    nome = input (" Seu nome completo: ").strip()
    senha = input (" Crie uma senha: ").strip()
    novo_usuario: dict = {
        "nome":        nome,
        "senha":       senha, 
        "saldo":       0.0, 
        "biblioteca":  [], 
        "carrinho":    [],
        "admin":       False
    }
    
    usuarios[login] = novo_usuario
    salvar_json(ARQUIVO_USUARIOS, usuarios)
    print (f"\n Parabéns usuário {login} sua conta foi criada com sucesso! ")
    return login, novo_usuario

"""
Login em uma conta já existente.
"""

def fazer_login (usuarios: dict) -> tuple[str, dict] | tuple[None, None]: 
    print ("\n~~~~ LOGIN ~~~~")
    login = input (" Login: ").strip().lower()
    senha = input (" Senha: ").strip()
    if login not in usuarios:
        print (" Usuário não encontrado. ")
        return None, None
    elif usuarios[login]["senha"] != senha:
        print (" Senha incorreta. ")
        return None, None
    else:
        print (f"\n Seja Bem-Vindo(a), {usuarios[login]['nome']}!")
        return login, usuarios[login]
    
"""
Adicionar um jogo ao carrinho fo usuário em onde de chegada. 
"""
def adicionar_ao_carrinho (usuario: dict, jogo:dict) -> None:
    if jogo["id"] in usuario["biblioteca"]:
        print (" Você já possui esse jogo na sua biblioteca. ")
        return 
    
    ids_carrinho = [item["id"] for item in usuario["carrinho"]]
    if jogo["id"] in ids_carrinho: 
        print (" Esse jogo já esta no seu carrinho.")
        return
    
    usuario["carrinho"].append({"id": jogo["id"], "titulo": jogo["titulo"], "preco": jogo["preco"]})
    print (f" Parabéns o jogo {jogo['titulo']} foi adicionado ao seu carrinho!")


"""
Retirar item do carrinho 
"""

def remover_do_carrinho (usuario: dict) -> None:
    if not usuario["carrinho"]:
        print (" Carrinho vazio.")
        return
    
    exibir_carrinho(usuario)
    try:
        index = int (input(" Número do item para remover (0 para cancelar): "))
        if index == 0:
            return
        if 1 <= index <= len(usuario["carrinho"]):
            removido = usuario["carrinho"].pop(index - 1)
            print (f" O jogo {removido['titulo']} já foi removido do seu carrinho.")
        else: 
            print (" Número Inválido.")
    except ValueError:
        print (" Entrada inválida.")

"""
Exibir os itens do carrinho e retornar o total 
"""

def exibir_carrinho (usuario: dict) -> float:
    print ("\n~~~~ SEU CARRINHO ~~~~")
    if not usuario["carrinho"]:
        print (" (Vazio)")
        return 0.0
    
    total: float = 0.0
    for i, item in enumerate(usuario["carrinho"], 1):
        print (f" {i}. {item['titulo']:<32} R${item['preco']:.2f}")
        total += item["preco"]
    
    print (f" {'~' * 40}")
    print (f" {'TOTAL:':<32} R${total:.2f}")
    return total

"""
Debitar saldo (ficticio), mover jogos para a biblioteca e registrar o pedido. esvaziar o carrinho. 
"""
def finalizar_compra (usuario: dict, login: str, catalogo: list[dict], pedidos: list[dict], usuarios: dict) -> None: 
    total = exibir_carrinho (usuario)
    if total == 0:
        return 
    
    print (f"\n Saldo atual: R${usuario['saldo']:.2f}")
    
    if usuario["saldo"] < total:
        print (f" Saldo insufiente. Faltam R${(total - usuario['saldo']):.2f}")
        return
    
    confirmacao: str = input (" Comfirmar compra? (s/n): ").strip().lower()
    if confirmacao != "s": 
        print (" Compra cancelada.")
        return
    
    jogos_comprados: list[str] = []
    while usuario["carrinho"]:
        item = usuario["carrinho"].pop(0)
        usuario["biblioteca"].append(item["id"])
        jogos_comprados.append(item["titulo"])

    usuario["saldo"] = round(usuario["saldo"] - total, 2)

    pedido = {
        "id":       len(pedidos) + 1,
        "usuario":  login,
        "jogos":    jogos_comprados,
        "total":    total,
        "data":     datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }

    pedidos.append(pedido)

    salvar_json(ARQUIVO_USUARIOS, usuarios)
    salvar_json(ARQUIVO_CATALOGO, catalogo)
    salvar_json(ARQUIVO_PEDIDOS,  pedidos)

    print (f"\n Compra realizada! {len(jogos_comprados)} jogo(s) adicionado(s) à sua biblioteca")
    print (f" Saldo restante: R${usuario['saldo']:.2f}")
    
"""
Exibir a biblioteca do usuário com os jogos que ele possui
"""

def exibir_biblioteca (usuario: dict, catalogo: list[dict]) -> None:
    print ("\n~~~~ SUA BIBLIOTECA ~~~~")
    if not usuario["biblioteca"]:
        print (" (Nenhum jogo ainda)")
        return
    for jogo_id in usuario["biblioteca"]:
        jogo = buscar_jogo_por_id(catalogo, jogo_id)
        if jogo:
            print (jogo['titulo'], jogo['genero'])

"""
Permitir que o usuário adicione saldo (ficticio) à conta
"""

def adicionar_saldo (usuario: dict, login: str, usuarios: dict) -> None:
    print (f"\n Saldo atual: R${usuario['saldo']:.2f}")
    try:
        valor: float = float(input(" Valor a adicionar: R$"))
        if valor <= 0:
            print (" O valor deve ser positivo.")
            return
        usuario["saldo"] = round (usuario["saldo"] + valor, 2)
        usuarios[login] = usuario
        salvar_json(ARQUIVO_USUARIOS, usuarios)
        print (f" Saldo atualizado: R${usuario['saldo']:.2f}")
    except ValueError:
        print (" Valor inválido. Digite apenas números.")

"""
(Admin) Exportar pedidos para o arquivo "CSV"
"""

def exportar_relatorio_csv (pedidos: list[dict]) -> None:
    if not pedidos: 
        print (" Nenhum pedido para exportar. ")
        return
    
    arquivo_csv: str = "relatorio_pedidos.csv"
    with open (arquivo_csv, "w", newline="", encoding="utf-8") as f:
        campos = ["id", "usuario", "jogos", "total", "data"]
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        for pedido in pedidos:
            linha = pedido.copy()
            linha["jogos"] = " | ".join (pedido["jogos"])
            writer.writerow(linha)

    print (f" Relatório exportado com sucesso para '{arquivo_csv}'")

"""
Remover jogo do catálogo pelo ID e também remove o jogo apagado da biblioteca de todos os usuários. 
"""

def remover_jogo (catalogo: list[dict], usuarios: dict) -> None:
    exibir_catalogo (catalogo)
    try:
        jogo_id = int(input(" ID do jogo para remover (0 para cancelar): "))
        if jogo_id == 0:
            return
        
        jogo = buscar_jogo_por_id (catalogo, jogo_id)
        if not jogo:
            print (" ID não encontrado.")
            return
        
        confirmacao = input(f" Remover {jogo['titulo']}? (s/n): ").strip().lower()
        if confirmacao != "s":
            print(" Operação Cancelada.")
            return
        
        catalogo.remove(jogo)

        for u in usuarios.values():
            if jogo_id in u["biblioteca"]:
                u["biblioteca"].remove(jogo_id)
            u["carrinho"] =[item for item in u["carrinho"] if item["id"] != jogo_id]

        salvar_json (ARQUIVO_CATALOGO, catalogo)
        salvar_json (ARQUIVO_USUARIOS, usuarios)
        print (f" O Jogo {jogo['titulo']} foi removido com sucesso.")

    except ValueError:
        print (" ID inválido.")

"""
Painel de Administrador: adicionar jogos, ver relatórios.
"""

def painel_admin (catalogo: list[dict], usuarios: dict, pedidos: list[dict]) -> None:
    while True: 
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~")
        print("|   🔧 PAINEL ADMIN     |")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("| 1. Ver todos usuários |")
        print("| 2. Ver todos pedidos  |")
        print("| 3. Adicionar jogo     |")
        print("| 4. Exportar CSV       |")
        print("| 5. Remover jogo       |")  
        print("| 6. Voltar             |")  
        print("~~~~~~~~~~~~~~~~~~~~~~~~~")

        opcao: str = input (" Opção: ").strip()

        if opcao == "1":
            print ("\n~~~~ USUÁRIO ~~~~")
            for login, u in usuarios.items():
                print (f" {login} | {u['nome']} | Saldo: R${u['saldo']:.2f} | Jogos: {len(u['biblioteca'])}")
        elif opcao == "2": 
            print ("\n~~~~ PEDIDOS ~~~~")
            if not pedidos:
                print (" (Nenhum Pedido)")
            for p in pedidos: 
                print (f" #{p['id']} | {p['usuario']} | {','.join(p['jogos'])} | R${p['total']:.2f} | {p['data']}")
        elif opcao == "3":
            try:
               titulo = input(" Título do jogo: ").strip()
               genero = input(" Gênero: ").strip()
               preco = float(input(" Preço: R$"))
               novo_id = max(j["id"] for j in catalogo) + 1
               catalogo.append({
                   "id":       novo_id,
                   "titulo":   titulo,
                   "genero":   genero,
                   "preco":    preco,
                   "avaliacao":0.0
               })
               salvar_json(ARQUIVO_CATALOGO, catalogo)
               print (f" O Jogo {titulo} foi adicionado com ID {novo_id}.")
            except ValueError: 
                print (" Dados Inválidos.")
        elif opcao == "4":
            exportar_relatorio_csv(pedidos)
        elif opcao == "5":
            remover_jogo(catalogo, usuarios)
        elif opcao == "6":
            break
        else:
            print (" Opção inválida.")

"""
Exibir e gerenciar menu principal do usuário. 
"""

def menu_usuario (login: str, usuario: dict, catalogo: list[dict], pedidos: list[dict], usuarios: dict) -> None:
    while True:
        print(f"\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"|    {login:<25}|")
        print(f"|    Saldo: R${usuario['saldo']:<16.2f}|")
        print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"| 1. Ver catálogo              |")
        print(f"| 2. Buscar por gênero         |")
        print(f"| 3. Adicionar ao carrinho     |")
        print(f"| 4. Ver/Remover carrinho      |")
        print(f"| 5. Finalizar compra          |")
        print(f"| 6. Minha biblioteca          |")
        print(f"| 7. Adicionar saldo           |")
        print(f"| 8. 🎲 Jogo recomendado       |")
        if usuario.get("admin"):
            print(f"| 9. 🔧 Painel Admin           |")
        print(f"| 0. Sair                      |")
        print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        opcao: str = input(" Opção: ").strip()

        if opcao == "1":
            exibir_catalogo(catalogo)
        
        elif opcao == "2":
            generos = list({j["genero"] for j in catalogo})
            print (" Gênero disponíveis: " + ", ".join(sorted(generos)))
            genero = input(" Digite o Gênero: ").strip()
            exibir_catalogo(catalogo, filtro_genero=genero)

        elif opcao == "3": 
            exibir_catalogo(catalogo)
            try:
                jogo_id = int(input(" ID do jogo: "))
                jogo = buscar_jogo_por_id(catalogo, jogo_id)
                if jogo:
                    adicionar_ao_carrinho(usuario,  jogo)
                else:
                    print (" ID não encontrado.")
            except ValueError:
                print(" ID Inválido.")

        elif opcao == "4": 
            exibir_carrinho(usuario)
            acao = input(" Deseja remover algum item? (s/n): ").strip().lower()
            if acao == "s":
                remover_do_carrinho(usuario)

        elif opcao == "5":
            finalizar_compra(usuario, login, catalogo, pedidos, usuarios)
        
        elif opcao  == "6":
            exibir_biblioteca(usuario, catalogo)
        
        elif opcao == "7":
            adicionar_saldo(usuario, login, usuarios)

        elif opcao == "8":
            recomendado = recomendar_jogo(catalogo)
            print (f"\n Recomendação do dia é: {recomendado['titulo']}")
            print (f" Gênero: {recomendado['genero']} | Preço: R${recomendado['preco']:.2f}  | Avaliação: {recomendado['avaliacao']}")
        
        elif opcao == "9":
            painel_admin(catalogo, usuarios, pedidos)
        
        elif opcao == "0":
            print (f"\n Até logo, {usuario['nome']}!")
            break

        else:
            print(" Opção Inválida.")

"""
Entrada Principal do sistema e apresentação do menu de acesso.
"""

def main() -> None:
    print ("~" * 60)
    print (" Seja Bem-Vindo ao Infinite Play - Loja de Jogos Online")
    print (f" {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print ("~" * 60)

    catalogo: list[dict] = carregar_json(ARQUIVO_CATALOGO, CATALOGO_INICIAL)
    usuarios: dict       = carregar_json(ARQUIVO_USUARIOS, {})
    pedidos:  list[dict] = carregar_json(ARQUIVO_PEDIDOS, [])

    if "admin" not in usuarios:
        usuarios["admin"] = {
            "nome":       "Adminstrador",
            "senha":      "admin123",
            "saldo":      0.0,
            "biblioteca": [],
            "carrinho":   [],
            "admin":      True
        }
        salvar_json(ARQUIVO_USUARIOS, usuarios)

    while True:
        print("~~~~~~~~~~~~~~~~~~~~~~~~")
        print("|   1. Entrar          |")
        print("|   2. Cadastrar       |")
        print("|   0. Encerrar        |")
        print("~~~~~~~~~~~~~~~~~~~~~~~~")

        escolha: str = input(" Opção: ").strip()

        if escolha == "1":
            login, usuario = fazer_login(usuarios)
            if login:
                menu_usuario(login, usuario, catalogo, pedidos, usuarios)

        elif escolha == "2":
            login, usuario = cadastro_usuario(usuarios)
            menu_usuario(login, usuario, catalogo, pedidos, usuarios)

        elif escolha == "0":
            total_jogos: int = floor(len(catalogo))
            print(f"\n  Sistema encerrado. Temos {total_jogos} jogos no nosso catálogo. Até mais!")
            break

        else:
            print("   Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()