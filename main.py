import os
import datetime

itens = {}
dia_hoje = datetime.date.today()

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

def listar_itens():
    if itens:
        print("\nItens cadastrados:")
        print(f"{'ID':>3}  {'Nome':<20}  {'Qtd':>5}   {'Val':>10}")
        print("-" * 50)
        for id_, dados in itens.items():
            val_str = dados['validade'].strftime("%d/%m/%Y")
            print(f"{id_:>3}  {dados['nome']:<20}  {dados['quantidade']:>5}   {val_str:>10}")
        print("-" * 50)    

# -------------- FUNÇÕES DE SISTEMA -------------- # 

def main_estoque():
    limpa_tela()
    print(itens)
    opc_menu = ['1','2','3','4','0']

    print("-=" * 17)
    print('''
        1) Cadastrar item
        2) Listar item
        3) Descontar item
        4) Comprar itens
        0) Sair
    ''')
    print("-=" * 17 + "\n")

    escolha = forca_opcao(opc_menu, 'Qual opção o usuário deseja acessar?:\n-> ')
    if escolha == "1":
        cadastro_item()
    elif escolha == "2":
        listar_item_cadastrados()
    elif escolha == "3":
        desconto()
    elif escolha == "4":
        compra()
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
    
    while True:
        s = input_nao_vazio("Validade do item (DD/MM/YYYY):\n-> ").strip()
        try:
            validade = datetime.datetime.strptime(s, "%d/%m/%Y").date()
        except ValueError:
            print("⚠️  Formato inválido. Use DD/MM/YYYY.")
            continue
        if validade < dia_hoje:
            print("⚠️  Validade menor que o dia atual.")
        else:
            break

    novo_id = len(itens) + 1
    itens[novo_id] = {"nome": nome, "quantidade": quantidade, "validade": validade}
    print(f"✅ Item cadastrado: ID {novo_id} → {nome} (Qtd: {quantidade} / Val: {validade.strftime('%d/%m/%Y')})")
    retorna_menu()

def listar_item_cadastrados():
    limpa_tela()
    if itens:
        listar_itens()
        retorna_menu()
    else:
        print("⛔ Nenhum item cadastrado ainda.")
        retorna_menu()

def desconto():
    limpa_tela()
    listar_itens()
    if not itens:
        print("⛔ Nenhum item cadastrado ainda.")
        retorna_menu()

    print('''
          0) ◀️ Voltar
          ''')

    while True:
        try:
            id_escolhido = int(input_nao_vazio("Digite o ID do item que deseja usar:\n-> "))
            if id_escolhido == 0:
                retorna_menu()
            elif id_escolhido not in itens:
                raise KeyError("ID não existe")
            elif itens[id_escolhido]["quantidade"] == 0:
                raise ValueError("sem estoque disponível")
        except ValueError or KeyError as e:
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
            elif qtd_usar > qtd_disponivel:
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

def compra():
    limpa_tela()
    if not itens:
        print("⛔ Nenhum item cadastrado ainda.")
        retorna_menu()

    listar_itens()
    print('''0) ◀️ Voltar''')

    while True:
        try:
            id_escolhido = int(input_nao_vazio("Digite o ID do item que deseja comprar (repor):\n-> "))
            if id_escolhido == 0:
                return retorna_menu()
            if id_escolhido not in itens:
                raise KeyError("ID não existe")
        except (ValueError, KeyError) as e:
            print(f"⚠️ Escolha inválida ({e}). Tente novamente.\n")
        else:
            break

    nome_item = itens[id_escolhido]["nome"]
    qtd_atual = itens[id_escolhido]["quantidade"]

    while True:
        try:
            qtd_compra = int(input_nao_vazio(
                f"Quantas unidades de '{nome_item}' você quer comprar? (Atualmente: {qtd_atual})\n-> "
            ))
            if qtd_compra <= 0:
                raise ValueError("deve ser maior que zero")
        except ValueError as e:
            print(f"⚠️ Quantidade inválida ({e}). Tente novamente.\n")
        else:
            break

    itens[id_escolhido]["quantidade"] += qtd_compra
    novo_total = itens[id_escolhido]["quantidade"]
    print(f"\n✅ Repostos {qtd_compra} unidade(s) de ID {id_escolhido} → {nome_item}.")
    print(f"   Novo total em estoque: {novo_total}")
    retorna_menu()

if __name__ == "__main__":
    main_estoque()