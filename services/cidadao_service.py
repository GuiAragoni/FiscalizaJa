import pandas as pd
from db.database_config import DataBase

class Cidadao:
    def __init__(self):
        db = DataBase(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER=Guiga\\SQLEXPRESS;DATABASE=FiscalizaJa;Trusted_Connection=yes;')
        self.cursor = db.connect()
        
    def obter_todos_os_dados(self):
        self.cursor.execute("SELECT * FROM Cidadao")
        
        rows = self.cursor.fetchall()

        colunas = [
            'IdCidadao',
            'Nome',
            'Email',
            'Telefone',
            'CPF',
            'Endereco'
        ]

        df = pd.DataFrame.from_records(rows, columns=colunas)

        return df
