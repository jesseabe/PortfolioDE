# Portfolio
Hi my name is Jessé Rodrigues, and welcome to my Github Portfolio.
This repo contains all of my Data Engineer projects.

Here is my LinkedIn: https://www.linkedin.com/in/jesse-abe/

Below, you can check a brief description of my projects.


## Project 1 - Data Quality with Python and Pandera

**Goal**: Create an ETL with dataframe validation.

**Description**:
In this project, I utilized Pandera to enforce data quality during the ETL process. Pandera's validation framework ensured that the data loaded into the database adhered to the predefined data contracts. This involved setting up data schemas and applying rigorous checks to maintain data integrity, thus preventing errors and inconsistencies in the data pipeline.

**Key Features**:

- Implementation of data validation rules using Pandera.
- Automation of the ETL process with Python.
- Ensuring compliance with data contracts.
- Enhanced data integrity and reliability.

**Technologies Used**:

- Python
- Pandera
- Pandas
- SQL (for database operations)
- Postgrees


## Project 2 - Input Validator with Streamlit and Pydantic

**Goal**: Receber arquivos xlsx de usuários não técnicos, realizar um tratamento e validar o schema do arquivo.

**Description**: Para o frontend, onde o usuário possa interagir com a interface e realizar o upload dos arquivos xlsx, utilizou-se a biblioteca Streamlit. Para realizar o ETL, utilizou-se pandas e para a validação do schema do arquivo carregado pelo usuário, utilizou-se a biblioteca pydantic, de forma que, caso haja algum desacordo em relação ao arquivo desejado e o enviado, o usuário receba uma mensagem de erro. 

**Key Features**:

- Implementation front end userfriendly with Streamlit 
- Implementation of data validation rules using Pydantic.
- Implementation ETL using Pandas

**Technologies Used**:

- Python
- Streamlit
- Pydantic
- Pandas


## Project 3 - Webscraping Competitive Intelligence with Scrapy

**Goal**: Realizar webscraping do site https://ead.unisinos.br, identificar os links de cada curso e iterar sobre a página de cada curso para extrair as informações de tipo_curso, curso, mensalidade_original,mensalidade_promo, duracao. Salvar os dados em um banco de dados e apresentar em um dashboard de Inteligência Competitiva.

**Description**: Para realizaro webscraping, utilizou-se a biblioteca Scrapy. Para a leitura e ETL dos dados utilizou-se a biblioteca Pandas. Como banco de dados utilizou-se SQLite3. Para o dashboard, utilizou-se a biblioteca Streamlit. 

**Key Features**:

- Webscraping with Scrapy
- ETL with Pandas
- SQL database with SQLite3
- Implementation dashboard with Streamlit

**Technologies Used**:

- Python
- Scrapy
- Streamlit
- Pandas
- SQLite3
- SQL

