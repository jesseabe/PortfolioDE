import pandas as pd
import sqlite3

def csv_to_sql(csv_path, db_path, name):
    df = pd.read_csv(csv_path)
    print(df.head())
    
    conn = sqlite3.connect(db_path)
    df.to_sql(name, conn, if_exists='append', index=False)
    conn.close()

    print("Base salva com sucesso")

if __name__ == "__main__":
    csv_to_sql("data/dre.csv", "data/dre.db", "dre")
