import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "data" / "kbmdatabase.db"

# ------------------------------------------------------------------------
# Função para inicializar o banco de dados e criar a tabela se não existir
# ------------------------------------------------------------------------
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_id TEXT NOT NULL UNIQUE,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            biggest_price REAL NOT NULL,
            lowest_price REAL NOT NULL,
            guaranteed_months INTEGER NOT NULL,
            quantity INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    
# --------------------------------------------------------
# Inicializa o banco de dados ao importar este módulo
# --------------------------------------------------------
init_db()
def connect_db():
    return sqlite3.connect(DB_PATH)