import datetime
import unittest

def adicionar_item(itens: dict, item: dict) -> None:
    """
    Adiciona um item ao dicionário de itens.
    Cada item deve ter chaves: id, nome, quantidade, validade, preco, fornecedor, categoria.
    """
    itens[item['id']] = item

# --- Testes unitários --- #

class ControleDeEstoque(unittest.TestCase):
    
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
    
    def setUp(self):
        self.itens = {}
        hoje = datetime.date(2025, 5, 22)
        self.hoje = hoje
        for item in exemplos:
            adicionar_item(self.itens, item)