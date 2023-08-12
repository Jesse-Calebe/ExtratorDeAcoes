import datetime
import os


class Log:
    def __init__(self) -> None:
        agora = datetime.datetime.now()

        caminho = os.getcwd() + r'\log'
        if not os.path.exists(caminho):
            os.makedirs(caminho)

        self.caminho = caminho + f'\\Log_{agora}.txt'
        print(self.caminho)
        with open('log.txt', 'w') as arquivo:
            arquivo.write('')
        
    def addLog(self, texto):
        agora = datetime.datetime.now()
        mensagem = f'{agora} >> {texto}\n'

        with open('log.txt', 'a') as arquivo:
            arquivo.write(mensagem)
