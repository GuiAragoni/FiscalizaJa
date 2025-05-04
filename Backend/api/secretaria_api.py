from flask import Flask, request, jsonify
from services.secretaria_service import Secretaria

app = Flask(__name__)
secretaria_service = Secretaria()


@app.route('/secretaria', methods=['GET'])
def listar_secretarias():
    try:
        df = secretaria_service.obter_todos()
        return app.response_class(
            response=df.to_json(orient='records', force_ascii=False),
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@app.route('/secretaria/<int:id>', methods=['GET'])
def obter_secretaria(id):
    try:
        df = secretaria_service.obter_por_id(id)
        if df.empty:
            return jsonify({'mensagem': 'Secretaria não encontrada'}), 404
        return jsonify(df.iloc[0].to_dict())
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@app.route('/secretaria', methods=['POST'])
def criar_secretaria():
    try:
        dados = request.json
        secretaria_service.inserir(dados)
        return jsonify({'mensagem': 'Secretaria criada com sucesso!'}), 201
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@app.route('/secretaria/<int:id>', methods=['PUT'])
def atualizar_secretaria(id):
    try:
        dados = request.json
        secretaria_service.atualizar(id, dados)
        return jsonify({'mensagem': 'Secretaria atualizada com sucesso!'}), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@app.route('/secretaria/<int:id>', methods=['DELETE'])
def deletar_secretaria(id):
    try:
        secretaria_service.deletar(id)
        return jsonify({'mensagem': 'Secretaria deletada com sucesso!'}), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
