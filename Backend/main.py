# main.py
from flask import Flask

app = Flask(__name__)

from rotas.cidadao import cidadao_bp
from rotas.ocorrencia import ocorrencia_bp
from rotas.secretaria import secretaria_bp
from rotas.tipoocorrencia import tipo_ocorencia_bp

app.register_blueprint(cidadao_bp)
app.register_blueprint(ocorrencia_bp)
app.register_blueprint(secretaria_bp)
app.register_blueprint(tipo_ocorencia_bp)

@app.route('/', methods=['GET'])  
def home():
    return ("Bem vindo ao sistema de gestão de cidadãos!<br>")

if __name__ == '__main__':
    app.run()
