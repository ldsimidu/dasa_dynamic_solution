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
     
def input_nao_vazio(mensagem):
    while True:
        variavel = input(mensagem)
        if variavel == "":
            print(f"⚠️ Texto não pode ser vazio")
        else:
            return variavel

def retorna_menu():
    input("\n\n◀️ Insira qualquer valor para voltar ao menu!")
    main_estoque()

def main_estoque():
    limpa_tela()
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

def cadastro_item():
    proximo_id = 1
    limpa_tela()
    nome = input_nao_vazio("Digite o nome do item:\n-> ")
    while True:
        quantidade = int(input_nao_vazio("Quantidade do item:\n-> ").strip())
        try:
            if quantidade <= 0:
                raise ValueError("deve ser maior que zero")

        except ValueError as e:
            print(f"⚠️ Quantidade inválida ({e}). Tente novamente.\n")
        else:
            break
    
    itens[proximo_id] = {"nome": nome, "quantidade": quantidade}
    print(f"✅ Item cadastrado: ID {proximo_id} → {nome} (Qtd: {quantidade})")
    
    retorna_menu()
    proximo_id += 1
    return proximo_id - 1

def listar_item():
    if itens:
        print("\nItens cadastrados:")
        print(f"{'ID':>3}  {'Nome':<20}  {'Qtd':>5}")
        print("-" * 32)
        for id_, dados in itens.items():
            print(f"{id_:>3}  {dados['nome']:<20}  {dados['quantidade']:>5}")
    else:
        print("⛔ Nenhum item cadastrado ainda.")

if __name__ == "__main__":
    main_estoque()