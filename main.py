import os
import datetime

# Estrutura global que armazena:
# - itens: dicionário de produtos com nome, quantidade e validade
# - memo: cache para memorização (programação dinâmica)
# - itens_ordenados_validade: lista auxiliar com itens ordenados por validade
estado = {
    'itens': {},
    'memo': {},
    'itens_ordenados_validade': []
}

# Data atual para comparações
dia_hoje = datetime.date.today()

# Limpa a tela do terminal de acordo com o sistema operacional
def limpa_tela():
    comando = 'cls' if os.name == 'nt' else 'clear'
    os.system(comando)

# Garante que o usuário escolha uma opção válida da lista
def forca_opcao(lista, mensagem):
    while True:
        escolha = input(mensagem)
        if escolha not in lista:
            print("⚠️  Escolha inválida")
        else:
            return escolha

# Solicita input até que um texto não vazio seja fornecido
def input_nao_vazio(mensagem):
    while True:
        variavel = input(mensagem)
        if variavel == "":
            print(f"⚠️ Texto não pode ser vazio")
        else:
            return variavel

# Aguarda o usuário pressionar Enter e retorna ao menu principal
def retorna_menu():
    input("\n\n◀️ Insira qualquer valor para voltar ao menu!")
    main_estoque()

# Lista todos os itens cadastrados com ID, nome, quantidade e validade
def listar_itens():
    if estado['itens']:
        print("\nItens cadastrados:")
        print(f"{'ID':>3}  {'Nome':<20}  {'Qtd':>5}   {'Val':>10}")
        print("-" * 50)
        for id_, dados in estado['itens'].items():
            val_str = dados['validade'].strftime("%d/%m/%Y")
            print(f"{id_:>3}  {dados['nome']:<20}  {dados['quantidade']:>5}   {val_str:>10}")
        print("-" * 50)

# Atualiza a lista de itens ordenada por validade
def atualizar_lista_ordenada():
    estado['itens_ordenados_validade'] = sorted(estado['itens'].items(), key=lambda x: x[1]['validade'])

# Calcula o total de itens em estoque com recursão + memorização
def estoque_total(ids=None):
    if ids is None:
        ids = list(estado['itens'].keys())
    ids_tuple = tuple(ids)

    if ids_tuple in estado['memo']:
        return estado['memo'][ids_tuple]
    if not ids:
        return 0

    primeiro = estado['itens'][ids[0]]['quantidade']
    restante = estoque_total(ids[1:])
    total = primeiro + restante
    estado['memo'][ids_tuple] = total
    return total

# Gera relatório com estatísticas do estoque
def relatorio_estoque():
    limpa_tela()
    if not estado['itens']:
        print("⛔ Nenhum item cadastrado ainda.")
        return retorna_menu()

    total_unidades = estoque_total()
    zerados = [item for item in estado['itens'].values() if item['quantidade'] == 0]
    proximos_vencimentos = [
        (id_, item) for id_, item in estado['itens'].items()
        if 0 <= (item['validade'] - dia_hoje).days <= 7
    ]
    quantidades = [item['quantidade'] for item in estado['itens'].values()]
    maior = max(quantidades)
    menor = min(quantidades)

    print("📦 RELATÓRIO DE ESTOQUE")
    print("-" * 50)
    print(f"🔢 Total de unidades em estoque: {total_unidades}")
    print(f"⚠️  Itens com quantidade zero: {len(zerados)}")
    print(f"📅 Itens com validade nos próximos 7 dias: {len(proximos_vencimentos)}")
    print(f"📈 Maior quantidade entre itens: {maior}")
    print(f"📉 Menor quantidade entre itens: {menor}")
    print("-" * 50)

    if proximos_vencimentos:
        print("\n📌 Vencimentos em breve:")
        for id_, item in proximos_vencimentos:
            dias = (item['validade'] - dia_hoje).days
            print(f"  - ID {id_}: {item['nome']} (em {dias} dias)")

    retorna_menu()

# Busca item pela data exata de validade
def buscar_por_validade_linear(data_alvo):
    for id_, dados in estado['itens'].items():
        if dados['validade'] == data_alvo:
            return id_, dados
    return None

# Menu principal do sistema
def main_estoque():
    limpa_tela()
    opc_menu = ['1','2','3','4','5','0']

    print("-=" * 17)
    print('''
        1) Cadastrar item
        2) Listar item
        3) Descontar item
        4) Comprar itens
        5) Relatório de Estoque
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
    elif escolha == "5":
        relatorio_estoque()
    elif escolha == "0":
        print("👋 Volte sempre! =)")

# Cadastra um novo item no estoque
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

    novo_id = len(estado['itens']) + 1
    estado['itens'][novo_id] = {"nome": nome, "quantidade": quantidade, "validade": validade}
    atualizar_lista_ordenada()
    estado['memo'] = {} # limpa cache de total
    print(f"✅ Item cadastrado: ID {novo_id} → {nome} (Qtd: {quantidade} / Val: {validade.strftime('%d/%m/%Y')})")
    retorna_menu()

# Lista itens ou informa ausência de itens
def listar_item_cadastrados():
    limpa_tela()
    if estado['itens']:
        listar_itens()
        retorna_menu()
    else:
        print("⛔ Nenhum item cadastrado ainda.")
        retorna_menu()

# Subtrai quantidade de um item em uso
def desconto():
    limpa_tela()
    listar_itens()
    if not estado['itens']:
        print("⛔ Nenhum item cadastrado ainda.")
        retorna_menu()

    print('''\n0) ◀️ Voltar''')

    while True:
        try:
            id_escolhido = int(input_nao_vazio("Digite o ID do item que deseja usar:\n-> "))
            if id_escolhido == 0:
                retorna_menu()
            elif id_escolhido not in estado['itens']:
                raise KeyError("ID não existe")
            elif estado['itens'][id_escolhido]["quantidade"] == 0:
                raise ValueError("sem estoque disponível")
        except (ValueError, KeyError) as e:
            print(f"⚠️ Não é possível usar este item ({e}). Escolha outro.\n")
        else:
            break

    nome_item = estado['itens'][id_escolhido]["nome"]
    qtd_disponivel = estado['itens'][id_escolhido]["quantidade"]

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

    estado['itens'][id_escolhido]["quantidade"] -= qtd_usar
    estado['memo'] = {} # limpa cache
    restante = estado['itens'][id_escolhido]["quantidade"]
    print(f"\n✅ Descontados {qtd_usar} unidade(s) de ID {id_escolhido} → {nome_item}.")
    print(f"   Quantidade restante: {restante}")
    retorna_menu()

# Aumenta a quantidade de um item (compra/reposição)
def compra():
    limpa_tela()
    if not estado['itens']:
        print("⛔ Nenhum item cadastrado ainda.")
        retorna_menu()

    listar_itens()
    print('''0) ◀️ Voltar''')

    while True:
        try:
            id_escolhido = int(input_nao_vazio("Digite o ID do item que deseja comprar (repor):\n-> "))
            if id_escolhido == 0:
                return retorna_menu()
            if id_escolhido not in estado['itens']:
                raise KeyError("ID não existe")
        except (ValueError, KeyError) as e:
            print(f"⚠️ Escolha inválida ({e}). Tente novamente.\n")
        else:
            break

    nome_item = estado['itens'][id_escolhido]["nome"]
    qtd_atual = estado['itens'][id_escolhido]["quantidade"]

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

    estado['itens'][id_escolhido]["quantidade"] += qtd_compra
    atualizar_lista_ordenada()
    estado['memo'] = {} # limpa cache
    novo_total = estado['itens'][id_escolhido]["quantidade"]
    print(f"\n✅ Repostos {qtd_compra} unidade(s) de ID {id_escolhido} → {nome_item}.")
    print(f"   Novo total em estoque: {novo_total}")
    retorna_menu()

# Inicia o programa
if __name__ == "__main__":
    main_estoque()
