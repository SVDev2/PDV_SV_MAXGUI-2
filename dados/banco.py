import sqlite3

def banco():
    return sqlite3.connect("caixa_SV.db")

def banco_caixa():
    con = banco()
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    estabelecimento INTEGER,
    login TEXT UNIQUE,
    senha_hash TEXT,
    ultimo_acesso TEXT,
    tipo TEXT
    )  
""")  

    cur.execute("""
    CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    produto TEXT,
    peso REAL,
    descricao TEXT,
    codigo TEXT UNIQUE,
    estoque REAL
    )  
""")  

    cur.execute("""
    CREATE TABLE IF NOT EXISTS estabelecimento (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cnpj_cpf TEXT,
    email TEXT,
    endereco TEXT
    )  
""")  
    con.commit()  
    con.close()