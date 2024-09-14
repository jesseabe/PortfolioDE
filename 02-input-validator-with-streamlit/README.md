# Input Validator With Pandera
Este projeto tem como objetivo coletar xlsx de usuários (não técnicos) e realizar a validação do arquivo antes de armazenar. Para este objetivo, opotou-se pelo desenvolvimento de um frontend utilizando streamlit e para a validação do schema e dos dados do arquivo, utilizou-se a biblioteca pydantic. 

![Data Quality Flow](images/InputValidator.png)

## Passos para a configuração e execução
1. Escolher a versão do python para 3.12.1
```bash
pyenv install 3.12.1
pyenv local 3.12.1
```

2. Criar um Abiente Virual
```bash
python3.12 -m venv .venv
```

3. Entrar no Ambiente Virtual
```bash
source .venv/bin/activate
```

4. Executar o Frontend
```bash
streamlit run app/main.py
```
