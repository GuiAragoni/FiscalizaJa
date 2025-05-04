import pandas as pd
from db.database_config import DataBase

class Ocorrencia:
    def __init__(self):
        db = DataBase()
        self.cursor = db.connect()

    def obter_todos(self):
        self.cursor.execute("SELECT * FROM Ocorrencia")
        rows = self.cursor.fetchall()
        colunas = [
            'IdOcorrencia', 'IdCidadao', 'IdSecretaria', 'IdTipoOcorrencia',
            'Localizacao', 'Titulo', 'Descricao', 'Foto', 'Prioridade',
            'Status', 'DataCriacao'
        ]
        return pd.DataFrame.from_records(rows, columns=colunas)

    def obter_por_id(self, id):
        self.cursor.execute("SELECT * FROM Ocorrencia WHERE IdOcorrencia = ?", id)
        row = self.cursor.fetchone()
        colunas = [
            'IdOcorrencia', 'IdCidadao', 'IdSecretaria', 'IdTipoOcorrencia',
            'Localizacao', 'Titulo', 'Descricao', 'Foto', 'Prioridade',
            'Status', 'DataCriacao'
        ]
        return pd.DataFrame([row], columns=colunas) if row else pd.DataFrame()

    def inserir(self, dados):
        self.cursor.execute("""
            INSERT INTO Ocorrencia (
                IdCidadao, IdSecretaria, IdTipoOcorrencia, Localizacao,
                Titulo, Descricao, Foto, Prioridade, Status, DataCriacao
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            dados['IdCidadao'], dados['IdSecretaria'], dados['IdTipoOcorrencia'],
            dados['Localizacao'], dados['Titulo'], dados['Descricao'],
            dados.get('Foto'), dados['Prioridade'], dados['Status'], dados['DataCriacao']
        ))
        self.cursor.commit()

    def atualizar(self, id, dados):
        self.cursor.execute("""
            UPDATE Ocorrencia SET
                IdCidadao = ?, IdSecretaria = ?, IdTipoOcorrencia = ?,
                Localizacao = ?, Titulo = ?, Descricao = ?,
                Foto = ?, Prioridade = ?, Status = ?, DataCriacao = ?
            WHERE IdOcorrencia = ?
        """, (
            dados['IdCidadao'], dados['IdSecretaria'], dados['IdTipoOcorrencia'],
            dados['Localizacao'], dados['Titulo'], dados['Descricao'],
            dados.get('Foto'), dados['Prioridade'], dados['Status'], dados['DataCriacao'], id
        ))
        self.cursor.commit()

    def deletar(self, id):
        self.cursor.execute("DELETE FROM Ocorrencia WHERE IdOcorrencia = ?", id)
        self.cursor.commit()
