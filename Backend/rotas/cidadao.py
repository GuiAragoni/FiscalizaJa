from flask import Blueprint, request, jsonify
from services.cidadao_service import Cidadao

cidadao_bp = Blueprint('cidadao', __name__)
cidadao_service = Cidadao()

@cidadao_bp.route('/cidadao', methods=['GET'])
def obter_cidadaos():
    try:
        df = cidadao_service.obter_todos_os_dados()
        return cidadao_bp.response_class(
            response=df.to_json(orient='records', force_ascii=False, date_format='iso'),
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        return jsonify({'erro': str(e)}), 500
      

@cidadao_bp.route('/cidadao/<int:id>', methods=['GET'])
def obter_cidadao_por_id(id):
    try:
        df = cidadao_service.obter_por_id(id)
        if df.empty:
            return jsonify({'mensagem': 'Cidadão não encontrado'}), 404
        return jsonify(df.iloc[0].to_dict())
    except Exception as e:
        return jsonify({'erro': str(e)}), 500
    

@cidadao_bp.route('/registrar', methods=['POST'])
def criar_cidadao():
    try:
        dados = request.json
        cidadao_service.inserir(dados)
        return jsonify({'mensagem': 'Cidadão criado com sucesso!'}), 201
    except Exception as e:
        return jsonify({'erro': str(e)}), 500
    

@cidadao_bp.route('/cidadao/<int:id>', methods=['PUT'])
def atualizar_cidadao(id):
    try:
        dados = request.json
        cidadao_service.atualizar(id, dados)
        return jsonify({'mensagem': 'Cidadão atualizado com sucesso!'}), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 500


@cidadao_bp.route('/cidadao/<int:id>', methods=['DELETE'])
def deletar_cidadao(id):
    try:
        cidadao_service.deletar(id)
        return jsonify({'mensagem': 'Cidadão deletado com sucesso!'}), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 500
