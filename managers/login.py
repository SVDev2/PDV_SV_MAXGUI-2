from datetime import datetime
from banco import *
import hashlib
import secrets

def gerar_hash(senha):
    return hashlib.sha256(senha.encode('utf-8')).hexdigest()
    
