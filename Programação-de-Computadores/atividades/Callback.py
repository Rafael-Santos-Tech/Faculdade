def pular():
    print("O jogador pulou!")

def atacar():
    print("O jogador atacou!")

def abrir_menu():
    print("Menu aberto!")

def verificar_evento(comando):

    if comando == "espaço":
        pular()

    elif comando == "mouse":
        atacar()

    elif comando == "esc":
        abrir_menu()

    else:
        print("Nenhum evento encontrado.")

while True:

    comando = input("Digite o comando: ").strip().lower()

    if comando == "sair":
        break

    verificar_evento(comando)
    