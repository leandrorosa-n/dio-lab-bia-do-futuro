# Passo a Passo de Execução

Esta pasta contém o código do seu agente financeiro.

## Setup do Ollama(5 minutos)

```
# 1. Instalar Ollama (ollama.com)
# 2. Baixar um modelo leve
ollama pull gpt-oss:20b

# 3. Testar se funciona
ollama run gpt-oss:20b


src/
├── app.py              # Aplicação principal (Streamlit/Gradio)
├── agente.py           # Lógica do agente
├── config.py           # Configurações (API keys, etc.)
└── requirements.txt    # Dependências
```

## Código completo

Todo o código-fonte está no arquivo 'app.py'


## Como Rodar

```bash
# 1. Instalar dependências
python -m pip install streamlit pandas requests

# 2. Garantir que Ollama está rodando
ollama serve

# 2. Rodar a aplicação
python -m streamlit run .\src\app.py
```
