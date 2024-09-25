import pandas as pd
import sqlite3

class PresencialDataProcessor:
    def __init__(self, csv_path, db_path):
        self.csv_path = csv_path
        self.db_path = db_path
        self.df_presencial = None

    def load_data(self):
        """Carrega os dados do arquivo CSV."""
        self.df_presencial = pd.read_csv(self.csv_path)
        print('Dados coletados')

    def clean_data(self):
        """Remove linhas onde o tamanho da string na coluna 'tipo_curso' é maior que 40 caracteres."""
        self.df_presencial = self.df_presencial[self.df_presencial['tipo_curso'].str.len() <= 40]

    def save_to_csv(self):
        """Salva o DataFrame processado de volta em um arquivo CSV."""
        self.df_presencial.to_csv(self.csv_path, index=False)

    def save_to_db(self):
        """Conecta ao banco de dados SQLite e salva os dados."""
        conn = sqlite3.connect(self.db_path)
        self.df_presencial.to_sql('cursos_presencial', conn, if_exists='replace', index=False)
        conn.close()

    def show_data(self, rows=5):
        """Exibe as primeiras linhas do DataFrame."""
        print(self.df_presencial.head(rows))

# Exemplo de uso
if __name__ == "__main__":
    processor_presencial = PresencialDataProcessor('data/cursos_presencial.csv', 'data/quotes.db')
    processor_presencial.load_data()
    processor_presencial.clean_data()
    processor_presencial.save_to_csv()
    processor_presencial.save_to_db()
    processor_presencial.show_data()