from flask import Flask
import pandas as pd

from db.database_config import DataBase

app = Flask(__name__)


@app.route('/home')
def index():
    db = DataBase(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER=Guiga\\SQLEXPRESS;DATABASE=FiscalizaJa;Trusted_Connection=yes;')
    cursor = db.connect()
    
    print("\nExemplo 1: Lendo dados da tabela Ocorrencia")
    cursor.execute("SELECT TOP 1 * FROM Ocorrencia")
    rows = cursor.fetchall()
    df = pd.DataFrame()

    colunas = [
        'IdOcorrencia',
        'IdCidadao',
        'IdSecretaria',
        'IdTipoOcorrencia',
        'Localizacao',
        'Titulo',
        'Descricao',
        'Foto',
        'Prioridade',
        'Status',
        'DataCriacao'
    ]

    # Criando o DataFrame
    df = pd.DataFrame.from_records(rows, columns=colunas)
    
    # Retornar como JSON com caracteres acentuados corretamente
    return app.response_class(
        response=df.to_json(orient='records', force_ascii=False, date_format='iso'),
        mimetype='application/json'
    )



if __name__ == '__main__':
    app.run(debug=True)

