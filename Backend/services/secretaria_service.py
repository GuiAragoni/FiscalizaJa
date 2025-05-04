import pandas as pd
from db.database_config import DataBase

class Secretaria:
    def __init__(self):
        db = DataBase()
        self.cursor = db.connect()

    def obter_todos(self):
        self.cursor.execute("SELECT * FROM Secretaria")
        rows = self.cursor.fetchall()
        colunas = [
            'IdSecretaria',
            'Instituicao',
            'Email',
            'Telefone',
            'CNPJ',
            'Estado',
            'Municipio'
        ]
        return pd.DataFrame.from_records(rows, columns=colunas)

    def obter_por_id(self, id_secretaria):
        self.cursor.execute("SELECT * FROM Secretaria WHERE IdSecretaria = ?", (id_secretaria,))
        rows = self.cursor.fetchall()
        colunas = [
            'IdSecretaria',
            'Instituicao',
            'Email',
            'Telefone',
            'CNPJ',
            'Estado',
            'Municipio'
        ]
        return pd.DataFrame.from_records(rows, columns=colunas)

    def inserir(self, dados):
        query = """
            INSERT INTO Secretaria (Instituicao, Email, Telefone, CNPJ, Estado, Municipio)
            VALUES (?, ?, ?, ?, ?, ?)
        """
        valores = (
            dados['Instituicao'],
            dados['Email'],
            dados['Telefone'],
            dados['CNPJ'],
            dados['Estado'],
            dados['Municipio']
        )
        self.cursor.execute(query, valores)
        self.cursor.commit()

    def atualizar(self, id_secretaria, dados):
        query = """
            UPDATE Secretaria
            SET Instituicao = ?, Email = ?, Telefone = ?, CNPJ = ?, Estado = ?, Municipio = ?
            WHERE IdSecretaria = ?
        """
        valores = (
            dados['Instituicao'],
            dados['Email'],
            dados['Telefone'],
            dados['CNPJ'],
            dados['Estado'],
            dados['Municipio'],
            id_secretaria
        )
        self.cursor.execute(query, valores)
        self.cursor.commit()

    def deletar(self, id_secretaria):
        self.cursor.execute("DELETE FROM Secretaria WHERE IdSecretaria = ?", (id_secretaria,))
        self.cursor.commit()
