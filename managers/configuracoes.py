import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def carregar_versao():
    caminho = BASE_DIR / "config-json" / "versao.json"

    with open(caminho, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)