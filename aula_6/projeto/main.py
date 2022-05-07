import json

from flask import Flask
from http import HTTPStatus
import requests


app = Flask(__name__)


# READ
@app.get("/get_info")
def get_info():
    """Essa função lê o banco de dados de informações do cliente"""
    with open("db.json", "r") as arquivo:
        arquivo = json.load(arquivo)
        return arquivo

# update
@app.post("/<string:cep>")
def save_info(cep):
    """Essa função atualiza o banco de dados"""
    json_coletada = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    return json_coletada.json()

app.run(port=5050)
