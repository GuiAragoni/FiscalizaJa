import pandas as pd
from db.database_config import DataBase

class Cidadao:
    def __init__(self):
        db = DataBase()
        self.cursor = db.connect()
        
    def obter_todos_os_dados(self):
        self.cursor.execute("SELECT * FROM Cidadao")
        rows = self.cursor.fetchall()
        colunas = ['IdCidadao', 'Nome', 'Email', 'Telefone', 'CPF', 'Endereco']
        return pd.DataFrame.from_records(rows, columns=colunas)

    def obter_por_id(self, id):
        self.cursor.execute("SELECT * FROM Cidadao WHERE IdCidadao = ?", id)
        row = self.cursor.fetchone()
        json_data = {
            'Nome': row[1],
            'Email': row[2],
            'CPF': row[3],
            'Telefone': row[4],
            'Endereco': row[5]
        } if row else None
        
        df = pd.DataFrame([json_data]) if json_data else pd.DataFrame()
        return df

    def inserir(self, dados):
        self.cursor.execute("""
            INSERT INTO Cidadao (Nome, Email, Telefone, CPF, Endereco)
            VALUES (?, ?, ?, ?, ?)
        """, (dados['Nome'], dados['Email'], dados['Telefone'], dados['CPF'], dados['Endereco']))
        self.cursor.commit()

    def atualizar(self, id, dados):
        self.cursor.execute("""
            UPDATE Cidadao
            SET Nome = ?, Email = ?, Telefone = ?, CPF = ?, Endereco = ?
            WHERE IdCidadao = ?
        """, (dados['Nome'], dados['Email'], dados['Telefone'], dados['CPF'], dados['Endereco'], id))
        self.cursor.commit()

    def deletar(self, id):
        self.cursor.execute("DELETE FROM Ocorrencia WHERE IdCidadao = ?", id)
        self.cursor.execute("DELETE FROM Cidadao WHERE IdCidadao = ?", id)
        self.cursor.commit()
