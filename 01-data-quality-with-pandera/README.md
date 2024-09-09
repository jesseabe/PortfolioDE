# Projeto de Qualidade em Dados

Este repositório contém um exemplo de um dos projetos que implementei no ambiente corporativo em uma das empresas em que trabalhei. O objetivo foi criar **contratos de dados**, a partir do entendimento do negócio, inputs e outputs desejados, e implementá-los dentro do pipeline **ETL** para que somente os dados que estejam de acordo com os contratos pré-definidos sejam enviados ao banco de dados.

## Objetivos principais:

1. **Definição de contratos de dados**:
   - Baseados no entendimento das necessidades do negócio.
   - Especificam as regras de qualidade que os dados precisam seguir.

2. **Implementação no pipeline ETL**:
   - Garantir que apenas dados válidos, de acordo com os contratos, sejam processados e enviados ao banco de dados.
   - Bloquear ou corrigir dados que não estejam em conformidade com os contratos, evitando a inserção de informações incorretas ou incompletas.

3. **Automatização do controle de qualidade**:
   - Integrar verificações automáticas dentro do pipeline para validar a integridade e a conformidade dos dados em tempo real.

Este processo assegura que o pipeline de dados seja confiável, reduzindo o risco de inconsistências no armazenamento de dados e melhorando os resultados analíticos para a empresa.

## Estrutura das Tabelas

A seguir estão descritas as principais tabelas utilizadas no projeto, com informações sobre o nome das colunas, o tipo de dados e as restrições aplicadas a cada campo.

### Tabela de Compras

| Nome da Coluna          | Tipo de Dados | Restrições                  |
|-------------------------|---------------|-----------------------------|
| Doc. Compra              | String        | Deve começar com 4          |
| Data                    | DateTime      | Nenhuma                     |
| Nome do Fornecedor       | String        | Não pode ser vazio           |
| ID do Material           | Int           | Deve ser maior que 0         |
| Descrição do Material    | String        | Não pode ser vazio           |
| Quantidade               | Float         | Deve ser maior que 0         |
| UMP                      | String        | Não pode ser vazio           |
| Montante                 | Float         | Deve ser maior que 0         |
| Moeda                    | String        | Não pode ser vazio           |
| Taxa de Câmbio           | Float         | Deve ser maior que 0         |

### Tabela de Vendas

| Nome da Coluna          | Tipo de Dados | Restrições                  |
|-------------------------|---------------|-----------------------------|
| Data                    | DateTime      | Nenhuma                     |
| ID do Material           | Int           | Deve ser maior que 0         |
| Descrição do Material    | String        | Não pode ser vazio           |
| Venda em Reais           | Float         | Deve ser maior que 0         |

### Tabela de Estoque

| Nome da Coluna          | Tipo de Dados | Restrições                  |
|-------------------------|---------------|-----------------------------|
| ID do Material           | Int           | Deve ser maior que 0         |
| Data                    | DateTime      | Nenhuma                     |
| Valor do Estoque         | Float         | Deve ser maior que 0         |
| Quantidade do Estoque    | Float         | Deve ser maior que 0         |
| UMB                      | String        | Nenhuma                     |





## Para rodar este projeto

**Definindo a versao do python**
```bash
pyenv local 3.12.1
```

**Ativando o ambiente virtual**
```bash
python -m venv .venv
```

```bash
source .venv/bin/activate
```

**Instalando as bibliotecas**
```bash
pip install pandas
pip install pandera
pip install pyodbc
pip install dotenv
pip install sqlalchemy
pip install datetime
```