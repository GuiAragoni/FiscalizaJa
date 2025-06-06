from flask import Blueprint, request, jsonify
from services.tipoocorrencia_service import TipoOcorrencia


tipo_ocorencia_bp = Blueprint('tipo_ocorencia', __name__)
tipo_service = TipoOcorrencia()

@tipo_ocorencia_bp.route('/tipoocorrencia', methods=['GET'])
def listar_tipos():
    try:
        df = tipo_service.obter_todos()
        return tipo_ocorencia_bp.response_class(
            response=df.to_json(orient='records', force_ascii=False),
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@tipo_ocorencia_bp.route('/tipoocorrencia/<int:id>', methods=['GET'])
def obter_tipo(id):
    try:
        df = tipo_service.obter_por_id(id)
        if df.empty:
            return jsonify({'mensagem': 'Tipo de ocorrência não encontrado'}), 404
        return jsonify(df.iloc[0].to_dict())
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@tipo_ocorencia_bp.route('/tipoocorrencia', methods=['POST'])
def criar_tipo():
    try:
        dados = request.json
        tipo_service.inserir(dados)
        return jsonify({'mensagem': 'Tipo de ocorrência criado com sucesso!'}), 201
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@tipo_ocorencia_bp.route('/tipoocorrencia/<int:id>', methods=['PUT'])
def atualizar_tipo(id):
    try:
        dados = request.json
        tipo_service.atualizar(id, dados)
        return jsonify({'mensagem': 'Tipo de ocorrência atualizado com sucesso!'}), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@tipo_ocorencia_bp.route('/tipoocorrencia/<int:id>', methods=['DELETE'])
def deletar_tipo(id):
    try:
        tipo_service.deletar(id)
        return jsonify({'mensagem': 'Tipo de ocorrência deletado com sucesso!'}), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 500
