# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores anteriores, ou seja, dar continuidade ao atendimento de forma mais efeciente|
| `perfil_comprador.json` | JSON | Personalizar explicações sobre dúvidas dos clientes |
| `produtos_loja.json` | JSON | Demonstrar produtos mais adequados ao cliente |
| `transacoes.csv` | CSV | Analisar padrão de compras do cliente |

> [!TIP]
> **Quer um dataset mais robusto?** Você pode utilizar datasets públicos do [Hugging Face](https://huggingface.co/datasets)

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

O produto Tênis STR foi substituído por Tênis LNR, pois estava mais aderente com as características dos produtos . Assim poderei validar respostas com o Leo de forma assertiva. 

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Existem duas possibilidades, injetar os dados diretamente no prompt (Ctrl + C, Ctrl + V) ou carregar os arquivos via código, como no exemplo abaixo.

```
Python

import pandas as pd
import json

# CSVs
historico = pd.read_csv('data/historico_atendimento.csv')
transacoes = pd.read_csv('data/transacoes.csv')

# JSONs
with open('data/Perfil_comprador.json', 'r', encoding='utf-8') as f:
    perfil = json.load(f)

with open('data/produtos_loja.json', 'r', encoding='utf-8') as f:
    produtos = json.load(f)
```

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

```text
DADOS DO CLIENTE:

PERFIL DO COMPRADOR:

TRANSAÇÕES:

PRODUTOS DA LOJA:
```

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Saldo disponível: R$ 5.000

Últimas transações:
- 01/11: Supermercado - R$ 450
- 03/11: Streaming - R$ 55
...
```
