import os

itens = {}

def limpa_tela():
    comando = 'cls' if os.name == 'nt' else 'clear'
    os.system(comando)

def forca_opcao(lista, mensagem):
    while True:
        escolha = input(mensagem)
        if escolha not in lista:
            print("⚠️  Escolha inválida")
        else:
            return escolha

def main_estoque():
    opc_menu = ['1', '2', '0']

    print('''
        1) Cadastrar utensílio
        2) Listar utensílios
        0) Sair\n
    ''')

    escolha = forca_opcao(opc_menu, 'Qual opção o usuário deseja acessar?:\n-> ')
    if escolha == "1":
        cadastro_item()
    elif escolha == "2":
        listar_item()
    elif escolha == "0":
        print("👋 Volte sempre! =)")

if __name__ == "__main__":
    main_estoque()