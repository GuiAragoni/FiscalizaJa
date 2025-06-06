# main.py
from flask import Flask, send_from_directory
from flasgger import Swagger
app = Flask(__name__)
from flask_cors import CORS

# Configuração do Flasgger
app.config['SWAGGER'] = {
    'title': 'FiscalizaJá API',
    'version': '1.0',
    'description': 'Documentação da API com Flasgger',
    'uiversion': 3  
}
swagger = Swagger(app)
CORS(app)

from rotas.cidadao import cidadao_bp
from rotas.ocorrencia import ocorrencia_bp
from rotas.secretaria import secretaria_bp


app.register_blueprint(cidadao_bp)
app.register_blueprint(ocorrencia_bp)
app.register_blueprint(secretaria_bp)


@app.route('/', methods=['GET'])  
def home():
    return ("Bem vindo ao sistema de gestão de cidadãos!<br>")

if __name__ == '__main__':
    app.run(debug=True)
