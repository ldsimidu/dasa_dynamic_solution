# 🏥 Solução DASA - Dynamic Programming

## 👩‍🎓 Alunos

| Nome                                   | RM       |
|----------------------------------------|----------|
| Bruna Costa Candeias                   | 558938   |
| Carlos Eduardo dos Santos Ribeiro Filho| 556785   |
| Lucas Derenze Simidu                   | 555931   |
| Marcos Vinícius da Silva Costa         | 555490   |
| Sofia Fernandes                        | 554873   |


## 🎯 Desafio Escolhido

**1ª Forma: Controle de Estoque com Estruturas de Dados e Programação Dinâmica**

---

## 🧠 Objetivo da Solução

Desenvolver um sistema de gerenciamento de estoque que simula a operação de uma unidade hospitalar, permitindo o cadastro, controle, reposição e análise de itens armazenados, com foco em performance e eficiência.  
A aplicação implementa técnicas de **programação dinâmica com memorização (_memoization_)** para otimizar cálculos recorrentes sobre os dados.

---

## 🧰 Tecnologias e Conceitos Aplicados

- **Linguagem:** Python 3  
- **Estruturas:** Dicionários, Listas, Listas de tuplas ordenadas  
- **Técnicas de Dynamic Programming:**  
  - ✅ Função recursiva com memorização para cálculo do estoque total (`estoque_total`)

### ⚙️ Funcionalidades Implementadas

- Cadastro de item com verificação de validade  
- Listagem de itens  
- Desconto de itens do estoque  
- Reposição de estoque  
- Geração de relatório completo com:
  - Total de unidades  
  - Itens vencendo em 7 dias  
  - Produtos zerados  
  - Maior e menor quantidade  
- **Validações e controle de fluxo:** menus interativos, validações robustas, uso de datas com `datetime`

---

## 🗃️ Estrutura de Dados

O estado do sistema é armazenado em um dicionário Python com a seguinte estrutura:

```python
estado = {
    'itens': {
        1: {
            'nome': 'Luvas Cirúrgicas',
            'quantidade': 50,
            'validade': datetime.date(2025, 6, 30)
        },
        ...
    },
    'memo': {},  # cache para memorização do estoque total
    'itens_ordenados_validade': []
}
```

---

## 🔁 Programação Dinâmica

A função `estoque_total()` é recursiva e utiliza **memorização** para evitar cálculos repetidos.  
Isso garante melhor desempenho ao calcular o total de unidades em estoque, conforme a lógica a seguir:

```python
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
```

---

## 📊 Análise Algorítmica e Complexidade

Esta seção descreve a eficiência computacional das funções implementadas no projeto, com foco em análise de tempo (complexidade) e técnicas de programação dinâmica aplicadas.

### 🔎 Resumo das Complexidades

| Função                         | Complexidade Temporal       | Observação Técnica                                          |
|-------------------------------|-----------------------------|-------------------------------------------------------------|
| `estoque_total()`             | `O(n)` (com memo)           | Programação dinâmica – recursiva com cache                 |
| `atualizar_lista_ordenada()` | `O(n log n)`                | Ordenação com TimSort                                      |
| `relatorio_estoque()`        | `O(n)`                      | Múltiplas operações lineares + memo reutilizado            |
| `cadastro_item()`            | `O(n log n)`                | Por causa da ordenação                                     |
| `compra()` / `desconto()`    | `O(n log n)`                | Também chamam ordenação após a modificação                 |
| `buscar_por_validade_linear()` | `O(n)`                    | Busca direta por data — linear                            |
| `listar_itens()`             | `O(n)`                      | Impressão sequencial                                       |

---

### ✅ Técnicas Aplicadas

- **Programação dinâmica (memoization)** → `estoque_total`
- **Ordenação eficiente (`TimSort`)** → `atualizar_lista_ordenada`
- **Busca linear** → `buscar_por_validade_linear`
- **Estrutura de dados eficiente (`dict`)** → acesso constante `O(1)`
- **Separação de responsabilidades e validações** → menu, entradas, fluxo

---

### 🧠 Detalhes por Função

#### `estoque_total()`
- Aplica **recursão com memorização**.
- Complexidade sem memo seria `O(2^n)`, mas com cache reduz para `O(n)`.

#### `atualizar_lista_ordenada()`
- Usa `sorted()` com TimSort: `O(n log n)`.

#### `relatorio_estoque()`
- Realiza várias iterações e cálculos com listas.
- Operações dominantes: `max()`, `min()`, `list comprehensions`: todas em `O(n)`.

#### `buscar_por_validade_linear()`
- Busca simples por data em dicionário: `O(n)`.

#### `cadastro_item()`, `compra()`, `desconto()`
- Operações de modificação com chamada à ordenação: `O(n log n)`.

#### `listar_itens()`
- Apenas imprime todos os itens: `O(n)`.

---

---

## ▶️ Como Executar

1. Certifique-se de ter o **Python 3** instalado em seu sistema.  
2. No terminal ou prompt de comando, execute:

```bash
python main.py
```

---


