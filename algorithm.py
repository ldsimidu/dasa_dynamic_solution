import datetime
import unittest

exemplos = [
        {'id': 1, 
         'nome': 'Seringa',
         'quantidade': 5,  
         'validade': datetime.date(2025, 5, 25), 
         'preco': 1.5,  
         'fornecedor': 'DASA',      
         'categoria': 'Medicina'},

        {'id': 2, 
         'nome': 'Algodão',           
         'quantidade': 10, 
         'validade': datetime.date(2025, 5, 20), 
         'preco': 0.5,  
         'fornecedor': 'Saúde+',    
         'categoria': 'Insumos'},

        {'id': 3, 
         'nome': 'Álcool',            
         'quantidade': 8,  
         'validade': datetime.date(2025, 6, 1), 
         'preco': 2.0,  'fornecedor': 'LabCorp',   
         'categoria': 'Limpeza'},

        {'id': 4, 
         'nome': 'Máscara',
         'quantidade': 20, 
         'validade': datetime.date(2025, 7, 1),  
         'preco': 0.75, 
         'fornecedor': 'MedPlus',   
         'categoria': 'Proteção'},

        {'id': 5, 
         'nome': 'Luvas Cirúrgicas',  
         'quantidade': 50, 
         'validade': datetime.date(2025, 4, 30),
         'preco': 0.2,  
         'fornecedor': 'SafeHands', 
         'categoria': 'Proteção'},

        {'id': 6, 
         'nome': 'Gaze',              
         'quantidade': 30, 
         'validade': datetime.date(2025, 5, 30),
         'preco': 0.1,  
         'fornecedor': 'Saúde+',    
         'categoria': 'Insumos'},
    ]

def adicionar_item(itens: dict, item: dict) -> None:
    """
    Adiciona um item ao dicionário de itens.
    Cada item deve ter chaves: id, nome, quantidade, validade, preco, fornecedor, categoria.
    """
    itens[item['id']] = item


def listar_itens(itens: dict) -> list:
    """Retorna a lista de itens cadastrados."""
    return list(itens.values())


def ordenar_por_validade(itens: dict, reverse: bool = False) -> list:
    items_list = list(itens.values())
    for i in range(1, len(items_list)):
        key_item = items_list[i]
        j = i - 1
        while j >= 0 and items_list[j]['validade'] > key_item['validade']:
            items_list[j + 1] = items_list[j]
            j -= 1
        items_list[j + 1] = key_item

    if reverse:
        return [items_list[i] for i in range(len(items_list) - 1, -1, -1)]
    return items_list


def filtrar_vencidos(itens: dict, hoje: datetime.date = None) -> list:
    """Retorna itens cuja validade já passou em relação a hoje."""
    hoje = hoje or datetime.date.today()
    return [i for i in itens.values() if i['validade'] < hoje]


def dias_para_vencimento(item: dict, hoje: datetime.date = None) -> int:
    """Retorna número de dias até o vencimento (negativo se já vencido)."""
    hoje = hoje or datetime.date.today()
    return (item['validade'] - hoje).days


def proximos_a_vencer(itens: dict, dias: int, hoje: datetime.date = None) -> list:
    """Retorna itens vencendo em até `dias` a partir de hoje."""
    hoje = hoje or datetime.date.today()
    return [i for i in itens.values() if 0 <= dias_para_vencimento(i, hoje) <= dias]


def valor_total(itens: dict) -> float:
    """Calcula o valor total do estoque (preco * quantidade)."""
    return sum(i['preco'] * i['quantidade'] for i in itens.values())


# --- Testes unitários --- #

class ControleDeEstoque(unittest.TestCase):

    def setUp(self):
        self.itens = {}
        hoje = datetime.date(2025, 5, 22)
        self.hoje = hoje
        for item in exemplos:
            adicionar_item(self.itens, item)

    def test_ordenacao_por_validade(self):
        ordenados = ordenar_por_validade(self.itens)
        datas = [i['validade'] for i in ordenados]
        esperado = [datetime.date(2025, 4, 30), datetime.date(2025, 5, 20), datetime.date(2025, 5, 25), datetime.date(2025, 5, 30), datetime.date(2025, 6, 1), datetime.date(2025, 7, 1)]
        self.assertEqual(datas, esperado)

    def test_ordenacao_por_validade_reverse(self):
        ordenados = ordenar_por_validade(self.itens, reverse=True)
        datas = [i['validade'] for i in ordenados]
        esperado = [datetime.date(2025, 7, 1), datetime.date(2025, 6, 1), datetime.date(2025, 5, 30), datetime.date(2025, 5, 25), datetime.date(2025, 5, 20), datetime.date(2025, 4, 30)]
        self.assertEqual(datas, esperado)

    def test_filtrar_vencidos(self):
        vencidos = filtrar_vencidos(self.itens, self.hoje)
        nomes = [i['nome'] for i in vencidos]
        self.assertListEqual(nomes, ['Algodão', 'Luvas Cirúrgicas'])

    def test_proximos_a_vencer(self):
        proximos = proximos_a_vencer(self.itens, 8, self.hoje)
        nomes = [i['nome'] for i in proximos]
        self.assertListEqual(nomes, ['Seringa', 'Gaze'])

    def test_valor_total(self):
        total = valor_total(self.itens)
        esperado = 5*1.5 + 10*0.5 + 8*2.0 + 20*0.75 + 50*0.2 + 30*0.1
        self.assertAlmostEqual(total, esperado)

if __name__ == '__main__':
    itens_demo = {}
    hoje = datetime.date(2025, 5, 22)

    for item in exemplos:
        adicionar_item(itens_demo, item)

    print("Itens cadastrados:")
    for i in listar_itens(itens_demo):
        print(f"- {i['nome']}: validade {i['validade'].strftime('%d/%m/%Y')}, qtd {i['quantidade']}")

    print("\nOrdenados por validade:")
    for i in ordenar_por_validade(itens_demo):
        print(f"- {i['nome']}: {i['validade'].strftime('%d/%m/%Y')}")

    print("\nItens vencidos:")
    for i in filtrar_vencidos(itens_demo, hoje):
        print(f"- {i['nome']} (vencido em {i['validade'].strftime('%d/%m/%Y')})")

    print("\nPróximos a vencer em até 8 dias:")
    for i in proximos_a_vencer(itens_demo, 8, hoje):
        dias = dias_para_vencimento(i, hoje)
        print(f"- {i['nome']}: em {dias} dias (válido até {i['validade'].strftime('%d/%m/%Y')})")

    print(f"\nValor total do estoque: R$ {valor_total(itens_demo):.2f}\n")

    unittest.main()
