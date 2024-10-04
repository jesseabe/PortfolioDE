# Portfolio Data Engineer
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

**Goal**: Receive xlsx files from non-technical users, perform processing and validate the file schema.

**Description**: For the frontend, where the user can interact with the interface and upload the xlsx files, the Streamlit library was used. To perform the ETL, pandas was used and to validate the schema of the file uploaded by the user, the pydantic library was used, so that if there is any disagreement in relation to the desired file and the one sent, the user receives an error message.

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

**Goal**: Perform webscraping of the website https://ead.unisinos.br, identify the links for each course and iterate over each course page to extract information on course_type, course, original_monthly_fee, promotional_monthly_fee, duration. Save the data in a database and present it in a Competitive Intelligence dashboard.

**Description**: To perform web scraping, the Scrapy library was used. For reading and ETL of the data, the Pandas library was used. SQLite3 was used as the database. For the dashboard, the Streamlit library was used.

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


## Project 4 - Deploy with Docker in AWS

**Goal**: Deploy an application to AWS using Docker.

**Description**: Code in streamlit, build the Docker image and deploy it to AWS.

**Technologies Used**:

- Docker
- AWS
- Python

## Project 5 - ETL with DuckDB: From Google Drive to PostgreSQL

**Goal**: Automate the process of downloading files from Google Drive, transforming the data, and loading it into a PostgreSQL database hosted on Render using DuckDB for data processing.

**Description**: This project involves downloading files in various formats (.csv, .parquet, and .json) from Google Drive, performing data transformations, applying business rules, and then uploading the processed data to a PostgreSQL database hosted on Render. DuckDB is used as an intermediary for efficient in-memory data processing and transformations before the final load into the PostgreSQL database.
**Technologies Used**:

- Duckdb
- Python
- SQL
- Render (Cloud)
- Postgres