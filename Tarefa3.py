from flask import Flask
from bd import produtos

app = Flash(__name__)

@app.route('/produtos',methods=['GET'])
def buscar_produtos():
    return make_response(
        jsonify(produtos)
    )

@app.route('/produtos',methods=['POST'])
def criar_produto():
    produto = request.json
    Produtos.append(produto)
    return make_response(
        jsonify(produtos)
    )

app.run()

