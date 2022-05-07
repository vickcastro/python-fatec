from flask import Flask
from http import HTTPStatus
import requests
import csv

app = Flask(__name__)


# READ
@app.get("/get_dados")
def get_info():
    """Essa função lê o banco de dados de informações do cliente"""
    with open("db.csv") as arquivo:
        arquivo_lido = csv.reader(arquivo, delimiter=",")
        linhas = []
        for linha in arquivo_lido:
            linhas.append(linha)


    return{"dados": linhas}

# update
@app.post("/")
def save_info():
    """Essa função atualiza o banco de dados"""
    pass

app.run(port=5050)
