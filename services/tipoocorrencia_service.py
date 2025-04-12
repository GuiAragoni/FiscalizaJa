import pandas as pd
from db.database_config import DataBase

class TipoOcorrencia:
    def __init__(self):
        db = DataBase()
        self.cursor = db.connect()

    def obter_todos(self):
        self.cursor.execute("SELECT * FROM TipoOcorrencia")
        rows = self.cursor.fetchall()
        colunas = ['IdTipoOcorrencia', 'IdSecretaria', 'Titulo', 'Descricao']
        df = pd.DataFrame.from_records(rows, columns=colunas)
        return df

    def obter_por_id(self, id):
        self.cursor.execute("SELECT * FROM TipoOcorrencia WHERE IdTipoOcorrencia = ?", id)
        row = self.cursor.fetchone()
        colunas = ['IdTipoOcorrencia', 'IdSecretaria', 'Titulo', 'Descricao']
        return pd.DataFrame([row], columns=colunas) if row else pd.DataFrame()

    def inserir(self, dados):
        self.cursor.execute("""
            INSERT INTO TipoOcorrencia (IdSecretaria, Titulo, Descricao)
            VALUES (?, ?, ?)
        """, (dados['IdSecretaria'], dados['Titulo'], dados['Descricao']))
        self.cursor.commit()

    def atualizar(self, id, dados):
        self.cursor.execute("""
            UPDATE TipoOcorrencia
            SET IdSecretaria = ?, Titulo = ?, Descricao = ?
            WHERE IdTipoOcorrencia = ?
        """, (dados['IdSecretaria'], dados['Titulo'], dados['Descricao'], id))
        self.cursor.commit()

    def deletar(self, id):
        self.cursor.execute("DELETE FROM TipoOcorrencia WHERE IdTipoOcorrencia = ?", id)
        self.cursor.commit()
