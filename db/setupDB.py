import sqlite3 as sql
import os


class SetupDB:
    @staticmethod
    def run():
        conexao = sql.connect(f'{os.getcwd()}\\db\\database.db')
        cursor  = conexao.cursor()
        
        camposSender = [
            'id integer primary key',
            'tipo text',
            'email text',
            'senha text'
        ]
        SetupDB.criaTabela(cursor, 'Emails', camposSender)

        print('Email do Sender')
        cursor.execute(f'INSERT INTO "Emails" VALUES (1, "sender", "{input("""Email: """)}", "{input("""Senha: """)}")')
        
        print('Email do Receiver')
        cursor.execute(f'INSERT INTO "Emails" VALUES (2, "receiver", "{input("""Email: """)}", "")')
        
        conexao.commit()
        conexao.close()

    @staticmethod
    def criaTabela(cursor, tabela, listCampos):
        cursor.execute(f'CREATE TABLE IF NOT EXISTS {tabela}({", ".join(listCampos)})')
