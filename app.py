from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'A origem da família e da propriedade privada.',
        'autor': 'Friedrich Engels',
        'editora': 'fodase',
        'ano': 2011,
    },
    {
        'id': 2,
        'titulo': 'Que Fazer?',
        'autor': 'Vladimir Lênin',
        'editora': 'fodase',
        'ano': 2011,
    },
    {
        'id': 3,
        'titulo': 'O Capital',
        'autor': 'Karl Marx',
        'editora': 'fodase',
        'ano': 2011,
    },
]

# Consultar livros (todos)

@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

# Consultar livro (por id)

@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

# Editar livro

@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

# Add livro

@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    novo_livro['id'] = len(livros) + 1
    livros.append(novo_livro)
    return jsonify({"mensagem": "Livro adicionado com sucesso", "livro": novo_livro}), 201

# Excluir livro

@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    
    return jsonify(livros)

if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)
