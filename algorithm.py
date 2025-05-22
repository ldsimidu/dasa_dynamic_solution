import datetime
import unittest

def adicionar_item(itens: dict, item: dict) -> None:
    """
    Adiciona um item ao dicionário de itens.
    Cada item deve ter chaves: id, nome, quantidade, validade, preco, fornecedor, categoria.
    """
    itens[item['id']] = item
