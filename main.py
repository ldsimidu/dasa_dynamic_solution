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
    opc_menu = ['1','2','3','0']

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
    elif escolha == "3":
        desconto()
    elif escolha == "0":
        print("👋 Volte sempre! =)")

def cadastro_item():
    limpa_tela()
    nome = input_nao_vazio("Digite o nome do item:\n-> ")
    while True:
        try:
            quantidade = int(input_nao_vazio("Quantidade do item:\n-> ").strip())
            if quantidade <= 0:
                raise ValueError("⚠️ Quantidade deve ser maior que zero.")
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
        print("-" * 32)
        retorna_menu()
    else:
        print("⛔ Nenhum item cadastrado ainda.")
        retorna_menu()

def desconto():
    limpa_tela()
    if not itens:
        print("⛔ Nenhum item cadastrado ainda.")
        retorna_menu()

    print("\nItens cadastrados:")
    print(f"{'ID':>3}  {'Nome':<20}  {'Qtd':>5}")
    print("-" * 32)
    for id_, dados in itens.items():
        print(f"{id_:>3}  {dados['nome']:<20}  {dados['quantidade']:>5}")
    print("-" * 32)
    print('''
          0) ◀️ Voltar
          ''')

    while True:
        try:
            id_escolhido = int(input_nao_vazio("Digite o ID do item que deseja usar:\n-> "))
            if id_escolhido == 0:
                retorna_menu()
            if id_escolhido not in itens:
                raise KeyError("ID não existe")
            if itens[id_escolhido]["quantidade"] == 0:
                raise ValueError("sem estoque disponível")
        except ValueError as e:
            print(f"⚠️ Não é possível usar este item ({e}). Escolha outro.\n")
        except KeyError as e:
            print(f"⚠️ Escolha inválida ({e}). Tente novamente.\n")
        else:
            break

    nome_item = itens[id_escolhido]["nome"]
    qtd_disponivel = itens[id_escolhido]["quantidade"]

    while True:
        try:
            qtd_usar = int(input_nao_vazio(
                f"Quantas unidades de '{nome_item}' você vai utilizar? (Disponível: {qtd_disponivel})\n-> "
            ))
            if qtd_usar <= 0:
                raise ValueError("deve ser maior que zero")
            if qtd_usar > qtd_disponivel:
                raise ValueError("maior que o disponível")
        except ValueError as e:
            print(f"⚠️ Quantidade inválida ({e}). Tente novamente.\n")
        else:
            break

    itens[id_escolhido]["quantidade"] -= qtd_usar
    restante = itens[id_escolhido]["quantidade"]
    print(f"\n✅ Descontados {qtd_usar} unidade(s) de ID {id_escolhido} → {nome_item}.")
    print(f"   Quantidade restante: {restante}")
    retorna_menu()


if __name__ == "__main__":
    main_estoque()