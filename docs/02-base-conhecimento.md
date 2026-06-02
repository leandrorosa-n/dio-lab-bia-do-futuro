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

Para simplificar, podemos simplesmente "injetar" os dados em nosso prompt, garantindo que o Agente tenha o melhor contexto possível. Lembrando que em soluções mais robustas o ideal 
é que essas informações sejam carregadas dinamicamente para que possamos ganhar flexibilidade.

```text
DADOS DO CLIENTE (Perfil_comprador.json):
{
  "nome": "João Silva",
  "idade": 32,
  "profissao": "Analista de Sistemas",
  "renda_mensal": 5000.00,
  "perfil_comprador": "moderado",
  "objetivo_principal": "comprar itens para o trabalho",
  "patrimonio_total": 15000.00,
  "reserva_emergencia_atual": 10000.00,
  "aceita_risco": false,
  "metas": [
    {
      "meta": "Ter estilo de vestimenta para reunioes de trabalho",
      "orcamento_real": 1200.00,
      "prazo": "2026-06"
    },
    {
      "meta": "Vestimenta para eventos",
      "orcamento_necessario": 1100.00,
      "prazo": "2027-12"
    }
  ]
}

PERFIL DO COMPRADOR (historico_atendimento.csv):
data,canal,tema,resumo,resolvido
2025-09-15,chat,créditos fiscais,Cliente perguntou sobre oportunidades e prazos,sim
2025-09-22,telefone,Problema no app,Erro ao visualizar extrato foi corrigido,sim
2025-10-01,chat,Imposto Federal,Cliente pediu explicação sobre o funcionamento do imposto federal,sim
2025-10-12,chat,Metas financeiras,Cliente acompanhou o progresso de créditos fiscais,sim
2025-10-25,email,Atualização cadastral,Cliente atualizou e-mail e telefone,sim

HISTÓRICO E ATENDIMENTO DO TRANSAÇÕES(historico_atendimento.csv):
data,canal,tema,resumo,resolvido
2025-09-15,chat,créditos fiscais,Cliente perguntou sobre oportunidades e prazos,sim
2025-09-22,telefone,Problema no app,Erro ao visualizar extrato foi corrigido,sim
2025-10-01,chat,Imposto Federal,Cliente pediu explicação sobre o funcionamento do imposto federal,sim
2025-10-12,chat,Metas financeiras,Cliente acompanhou o progresso de créditos fiscais,sim
2025-10-25,email,Atualização cadastral,Cliente atualizou e-mail e telefone,sim

PRODUTOS DA LOJA(produtos_loja.json):
[
  {
    "nome": "Bota SRT",
    "categoria": "calçado",
    "risco": "baixo",
    "conforto": "medio",
    "valor": 450.00,
    "indicado_para": "mulheres que buscam maior protecao no frio"
  },
  {
    "nome": "Sapatilha",
    "categoria": "rasteiras",
    "risco": "baixo",
    "conforto": "baixo",
    "valor": 55.90,
    "indicado_para": "Qmulheres que buscam maior praticidade"
  },
  {
    "nome": "Salto alto",
    "categoria": "plataforma",
    "risco": "baixo",
    "conforto": "medio",
    "valor": 120.00,
    "indicado_para": "mulheres que buscam melhora no estilo"
  },
  {
    "nome": "Tênis OLD",
    "categoria": "atrf",
    "risco": "medio",
    "conforto": "alto",
    "valor": 180.00,
    "indicado_para": "pessoas que buscam conforto em suas atividades diárias"
  },
  {
    "nome": "Tênis",
    "categoria": "atrf",
    "risco": "alto",
    "conforto": "Variável",
    "valor": 1200.00,
    "indicado_para": "pessoas que buscam conforto em dias corridos"
  }
]

```

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

O exemplo do contexto montado abaixo, se baseia nos dados originais da base de conhecimento, mas os sintetiza deixando apenas as informações mais importantes, otimizando assim o consumo de tokens.

```
DADOS DO CLIENTE:
- Nome: Guilherme Silva
- Perfil: Moderado
- Objetivo: comprar itens para o trabalho
- Orçamento: 2500,00 (meta: 6.000,00)

ÚLTIMAS COMPRAS:
- Tênis: 1200,00
- Bota: 450,00
- Sandalha: 55,90

ÚLTIMAS TRANSAÇÕES:
- 01/11: Tênis - R$ 780,00
- 03/11: Salto alto - R$ 170,00

```
