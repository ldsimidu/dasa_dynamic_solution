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

# -------------- FUNÇÕES DE SISTEMA -------------- # 

def main_estoque():
    limpa_tela()
    opc_menu = ['1','2','0']

    print("-=" * 17)
    print('''
        1) Cadastrar item
        2) Listar item
        3) Descontar item
        0) Sair
    ''')
    print("-=" * 17 + "\n")

    escolha = forca_opcao(opc_menu, 'Qual opção o usuário deseja acessar?:\n-> ')
    if escolha == "1":
        cadastro_item()
    elif escolha == "2":
        listar_item()
    elif escolha == "0":
        print("👋 Volte sempre! =)")

def cadastro_item():
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
    
    novo_id = len(itens) + 1
    itens[novo_id] = {"nome": nome, "quantidade": quantidade}
    print(f"✅ Item cadastrado: ID {novo_id} → {nome} (Qtd: {quantidade})")
    retorna_menu()

def listar_item():
    limpa_tela()
    if itens:
        print("\nItens cadastrados:")
        print(f"{'ID':>3}  {'Nome':<20}  {'Qtd':>5}")
        print("-" * 32)
        for id_, dados in itens.items():
            print(f"{id_:>3}  {dados['nome']:<20}  {dados['quantidade']:>5}")
        retorna_menu()
    else:
        print("⛔ Nenhum item cadastrado ainda.")
        retorna_menu()

if __name__ == "__main__":
    main_estoque()