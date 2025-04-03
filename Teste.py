import pandas as pd
from flask import Flask
from services.cidadao_service import Cidadao

app = Flask(__name__)
cidadao_service = Cidadao()



@app.route('/cidadao', methods=['GET'])
def obter_cidadao():
    try:
    
        df = cidadao_service.obter_todos_os_dados()
        df = df.drop(columns=['IdCidadao'], axis=1)

        return app.response_class(
            response=df.to_json(orient='records', force_ascii=False, date_format='iso'),
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        return app.response_class(
            response=str(e),
            status=500
        )


if __name__ == '__main__':
    app.run(debug=True)

