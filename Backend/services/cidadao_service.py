import pandas as pd
from db.database_config import DataBase

class Cidadao:
    def __init__(self):
        db = DataBase()
        self.cursor = db.connect()
        
    def obter_todos_os_dados(self):
        self.cursor.execute("SELECT * FROM Cidadao")
        rows = self.cursor.fetchall()
        colunas = ['IdCidadao', 'Nome', 'Email', 'Senha', 'CPF', 'Telefone', 'Endereco']
        return pd.DataFrame.from_records(rows, columns=colunas)

    def obter_por_id(self, id):
        self.cursor.execute("SELECT * FROM Cidadao WHERE IdCidadao = ?", id)
        row = self.cursor.fetchone()
        json_data = {
            'Nome': row[1],
            'Email': row[2],
            'Senha': row[3],
            'Cpf': row[4],
            'Telefone': row[5],
            'Estado': row[6],
            'Cidade': row[7]
        } if row else None
        
        df = pd.DataFrame([json_data]) if json_data else pd.DataFrame()
        return df
    
#region Obtem Dados Login
    def obter_dados_login(self, cpfEmail):
        self.cursor.execute("SELECT Nome, Email, Senha, CPF, Telefone, Estado, Cidade FROM Cidadao WHERE Email = ? Or CPF = ?", (cpfEmail, cpfEmail))
        row = self.cursor.fetchone()
        json_data = {
            'Nome': row[0],
            'Email': row[1],
            'Senha': row[2],
            'CPF': row[3],
            'Telefone': row[4],
            'Estado': row[5],
            'Cidade': row[6]
        } if row else None
        
        df = pd.DataFrame([json_data]) if json_data else pd.DataFrame()
        return df
#endregion
    
#region Registra Cidadao
    def inserir(self, dados):
        self.cursor.execute("""
            INSERT INTO Cidadao (Nome, Email, Senha, CPF, Telefone, Estado, Cidade)
            VALUES (?, ?, ?,?, ?, ?, ?)""", 
            (dados['Nome'], dados['Email'], dados['Senha'],dados['Cpf'],dados['Telefone'],dados['Estado'],dados['Cidade']))
        self.cursor.commit()        
#endregion

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
