import os
from dotenv import load_dotenv
import pyodbc
from sqlalchemy import create_engine
import pandas as pd

load_dotenv()

class DatabaseConnection:
    def __init__(self):
        self.server = os.environ.get("SERVER")
        self.database = os.environ.get("DATABASE")
        self.username = os.environ.get("USER_NAME")
        self.password = os.environ.get("PASSWORD")
        self.driver = os.environ.get("DRIVER")
        self.connect = None
        self.cursor = None

    def __enter__(self):
        self.connect = pyodbc.connect(
            f'DRIVER={self.driver};SERVER={self.server};PORT=1433;DATABASE={self.database};UID={self.username};PWD={self.password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
        )
        self.cursor = self.connect.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()
        if self.connect:
            self.connect.close()

    def create_table(self, table_name, create_sql):
        self.cursor.execute(create_sql)
        self.connect.commit()

    def insert_data(self, insert_sql, data):
        for row in data:
            self.cursor.execute(insert_sql, row)
        self.connect.commit()

    def get_connection_str(self):
        return self.connect



class SQLAlchemyConnection:
    def __init__(self):
        self.server = os.environ.get("SERVER")
        self.database = os.environ.get("DATABASE")
        self.username = os.environ.get("USER_NAME")
        self.password = os.environ.get("PASSWORD")
        self.driver = os.environ.get("DRIVER")

        # Cria uma string de conexão DSN diretamente
        self.dsn_connection_string = (
            f'DRIVER={self.driver};'
            f'SERVER={self.server};'
            f'DATABASE={self.database};'
            f'UID={self.username};'
            f'PWD={self.password};'
            'Encrypt=yes;'
            'TrustServerCertificate=no;'
            'Connection Timeout=30;'
        )

        self.engine = None
        self.connect = None

    def __enter__(self):
        # Inicializa a conexão pyodbc para garantir que o ODBC funcione
        self.connect = pyodbc.connect(self.dsn_connection_string)
        
        # Cria o engine SQLAlchemy usando a string de conexão DSN
        self.engine = create_engine(f'mssql+pyodbc:///?odbc_connect={self.dsn_connection_string}')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.engine:
            self.engine.dispose()
        if self.connect:
            self.connect.close()

    def to_sql(self, df, table_name, if_exists='replace'):
        df.to_sql(table_name, self.engine, if_exists=if_exists, index=False)