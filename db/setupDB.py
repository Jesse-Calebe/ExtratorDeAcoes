import sqlite3 as sql
import os


class SetupDB:
    def run():
        def criaTabela(cursor, tabela, listaCampos):
            camposTexto = ''

            for campo in listaCampos:
                camposTexto += campo + ', '
            
            camposTexto = camposTexto[0:-2]
                
            cursor.execute(f'CREATE TABLE IF NOT EXISTS {tabela}({camposTexto})')


        path = r'{}\db\database.db'.format(os.getcwd())

        conexao = sql.connect(path)
        cursor  = conexao.cursor()

        camposSender = [
            'id integer primary key',
            'email text',
            'senha text'
        ]

        criaTabela(cursor, 'Sender', camposSender)

        email = input('Email: ')
        senha = input('Senha: ')

        cursor.execute(f'INSERT INTO "Sender" ("id", "email", "senha") VALUES (1, "{email}", "{senha}")')
        conexao.commit()


        conexao.close()