import sqlite3 as sql
import os


class SetupDB:
    @staticmethod
    def run():
        conexao = sql.connect(f'{os.getcwd()}\\db\\database.db')
        cursor  = conexao.cursor()
        
        camposSender = [
            'id integer primary key',
            'email text',
            'senha text'
        ]
        SetupDB.criaTabela(cursor, 'Sender', camposSender)

        cursor.execute(f'INSERT INTO "Sender" VALUES (1, "{input("""Email: """)}", "{input("""Senha: """)}")')
        
        conexao.commit()
        conexao.close()

    @staticmethod
    def criaTabela(cursor, tabela, listCampos):
        cursor.execute(f'CREATE TABLE IF NOT EXISTS {tabela}({", ".join(listCampos)})')