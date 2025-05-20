from flask import Blueprint, request, jsonify
from services.ocorrencia_service import Ocorrencia

ocorrencia_bp = Blueprint('ocorrencia', __name__)
ocorrencia_service = Ocorrencia()

@ocorrencia_bp.route('/ocorrencia', methods=['GET'])
def listar_ocorrencias():
    try:
        df = ocorrencia_service.obter_todos()
        return ocorrencia_bp.response_class(
            response=df.to_json(orient='records', force_ascii=False),
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@ocorrencia_bp.route('/ocorrencia/<int:id>', methods=['GET'])
def obter_ocorrencia(id):
    try:
        df = ocorrencia_service.obter_por_id(id)
        if df.empty:
            return jsonify({'mensagem': 'Ocorrência não encontrada'}), 404
        return jsonify(df.iloc[0].to_dict())
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@ocorrencia_bp.route('/ocorrencia', methods=['POST'])
def criar_ocorrencia():
    try:
        dados = request.json
        ocorrencia_service.inserir(dados)
        return jsonify({'mensagem': 'Ocorrência criada com sucesso!'}), 201
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@ocorrencia_bp.route('/ocorrencia/<int:id>', methods=['PUT'])
def atualizar_ocorrencia(id):
    try:
        dados = request.json
        ocorrencia_service.atualizar(id, dados)
        return jsonify({'mensagem': 'Ocorrência atualizada com sucesso!'}), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@ocorrencia_bp.route('/ocorrencia/<int:id>', methods=['DELETE'])
def deletar_ocorrencia(id):
    try:
        ocorrencia_service.deletar(id)
        return jsonify({'mensagem': 'Ocorrência deletada com sucesso!'}), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 500
