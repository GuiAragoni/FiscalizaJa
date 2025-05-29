import pyodbc
import pandas as pd
from datetime import datetime

class DataBase:
    def __init__(self):
        
        #string fabricio
        #self.conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER=FIALHO\\SQLEXPRESS;DATABASE=FiscalizaJa;Trusted_Connection=yes;'
        
        #--------------------------
        #string gui
        self.conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER=Guiga\\SQLEXPRESS;DATABASE=FiscalizaJa;Trusted_Connection=yes;'

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