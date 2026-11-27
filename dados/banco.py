import sqlite3

def banco():
    return sqlite3.connect("caixa_SV.db")

def banco_caixa():
    con = banco()
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    estabelecimento_id INTEGER,
    nome TEXT UNIQUE,
    senha_hash TEXT,
    ultimo_acesso TEXT,
    tipo TEXT,
    estado TEXT
    )  
""")  

    cur.execute("""
    CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    estabelecimento_id INTEGER,
    categoria TEXT,
    produto TEXT,
    unidade REAL,
    descricao TEXT,
    codigo TEXT,
    preco_cliente REAL,
    preco_custo REAL,
    estoque REAL
    )  
""")
# unidade = unidade de medida (kg, ml, kilo, litro, etc.)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS estabelecimento (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    estabelecimento_id INTEGER,
    cnpj_cpf TEXT UNIQUE,
    email TEXT,
    senha_hash TEXT,
    estado TEXT,
    pais_de_atuacao TEXT
    )  
""")
# estado = ativo / inativo

    cur.execute("""
    CREATE TABLE IF NOT EXISTS caixas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    estabelecimento_id INTEGER,
    operador_id INTEGER,
    aberto_em TEXT,
    fechado_em TEXT,
    valor_abertura REAL,
    valor_fechamento REAL
    )  
""")
    con.commit()  
    con.close()