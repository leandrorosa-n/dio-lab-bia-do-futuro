# instale "python -m pip install streamlit pandas requests" no terminal
# "python -m streamlit run .\src\App.py" - no terminal


import json
import streamlit as st
import pandas as pd
import requests


# =========== CONFIGURAÇÃO ===========
OLLAMA_URL = "http://localhost:12345/api/generate"
MODELO = "gpt-oss:20b"


# ========== CARREGAR DADOS ==========
perfil = json.load(open('./data/perfil_comprador.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_loja.json'))



# =========== MONTAR CONTEXTO ===========
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_comprador']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# =========== SYSTEM PROMPT ===========
SYSTEM_PROMPT = """Você é o Leo, um educador tributário, especializado em ensinar conceitos de tributação de forma simples e prática

OBJETIVO:
Ensinar conceitos de tributação de forma simples, usando dados do fornecedor e com exemplos práticos.

REGRAS:
- Nunca recomende vendas específicas que deve fazer com base nos impostos;
- Jamais responda as perguntas fora do tema ensino de tributação;
- Quando ocorrer, responda lembrando o seu papel de educador tributário;
- Use dados fornecidos para dar exemplos personalizados;
- Linguagem simples, como se explicasse para um amigo;
- Se não souber algo, admita: "Não tenho essa informação, mas posso explicar...";
- Sempre pergunte se o cliente entendeu;
- Responda de forma sucinta e direta, com no máximo 3 parágrafos.
"""

# =========== CHAMAR OLLAMA ===========
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    {contexto}

Pergunta: {msg}"""
    
    r = requests.post(OLLAMA_URL, json={
        "model": MODELO,
        "prompt": prompt,
        "stream": False
    })
    return r.json()['response']


# =========== INTERFACE - CHATBOT=========== 
st.title("💸 Leo, seu Educador Tributário")

if pergunta := st.chat_input("Sua dúvida sobre tributação..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))


