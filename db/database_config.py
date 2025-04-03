import pyodbc
import pandas as pd
from datetime import datetime

class DataBase:
    def __init__(self, conn_str):
        self.conn_str = conn_str

    def connect(self):
        try:
            self.conn = pyodbc.connect(self.conn_str)
            self.cursor = self.conn.cursor()
            print("Conexão bem-sucedida com o SQL Server!")
            
            return self.cursor

        except pyodbc.Error as e:
            print(f"Erro na conexão: {e}")

    def close(self):
        if hasattr(self, 'conn'):
            self.conn.close()
            print("Conexão encerrada.")