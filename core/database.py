import sqlite3
import pandas as pd
import os

# --- CONFIGURAÇÃO DE CAMINHOS ---
# Define o caminho para a pasta 'data' relativa ao local deste script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "..", "data")
DB_PATH = os.path.join(DATA_DIR, "kbmdatabase.db")
EXCEL_PATH = os.path.join(DATA_DIR, "hardware_products.xlsx")

# Garante que a pasta data exista
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# --- CONEXÃO COM O BANCO ---
# Conecta ao banco de dados dentro da pasta 'data'
banco = sqlite3.connect(DB_PATH)
cursor = banco.cursor()

# Criação da tabela (caso não exista)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY, 
        name TEXT, 
        quantity INTEGER, 
        numberOfRatings INTEGER, 
        scoreOfRatings INTEGER,
        price REAL, 
        link TEXT, 
        imageUrl TEXT, 
        warranty TEXT
    )
""")

# --- PROCESSAMENTO DOS DADOS ---
try:
    # Carrega o arquivo Excel gerado pelo scraper
    print(f"Lendo arquivo: {EXCEL_PATH}")
    df = pd.read_excel(EXCEL_PATH)
    
    # Lista para controle de duplicatas durante a execução do script
    ids_processados = []

    # Itera sobre cada linha do DataFrame
    for index, row in df.iterrows():
        id_prod = row["ID"]
        nome_prod = row["Name"]
        
        # Prepara a tupla com os valores para inserção
        values = (
            id_prod, 
            nome_prod, 
            row["Quantity Available"], 
            row["Number of Ratings"], 
            row["Score of Ratings"], 
            row["Price"], 
            row["URL"], 
            row["Photos (g)"], 
            row["Warranty"]
        )

        # Verifica se o ID já foi processado neste loop
        if id_prod not in ids_processados:
            print(f"[{index}] Inserindo produto: {nome_prod}")
            
            try:
                query = "INSERT INTO products VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
                cursor.execute(query, values)
                ids_processados.append(id_prod)
            except sqlite3.IntegrityError:
                # Caso o ID já exista fisicamente no banco de dados (Primary Key)
                print(f"Aviso: ID {id_prod} já existe no banco de dados. Pulando...")
        else:
            print(f"Aviso: ID {id_prod} duplicado no Excel. Ignorado.")

    # Salva as alterações no banco de dados
    banco.commit()
    print("\nProcesso concluído com sucesso e dados salvos!")

except FileNotFoundError:
    print(f"Erro: O arquivo Excel não foi encontrado em {EXCEL_PATH}")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
finally:
    # Fecha a conexão com o banco
    banco.close()