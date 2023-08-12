import pandas
import os


class GeradorExcel:
    def __init__(self) -> None:
        self.columns = {
            'FII': ['ativos', 'setor', 'ticker', 'liquidezmediadiaria', 'pvp', 
                    'dividendo', 'yeld', 'media_yield_3m', 'media_yield_6m',
                    'media_yield_12m', 'soma_yield_3m', 'soma_yield_6m', 'soma_yield_12m',
                    'v_fisica',	'v_financeira', 'post_title']
        }
        
    def listToExcel(self, nomeArquivo, dados, tipo):
        linhasExcel = []
        
        for linha in dados:
            linhasExcel.append(linha)
        
        caminho = os.getcwd() + r'\extracoes'
        if not os.path.exists(caminho):
            os.makedirs(caminho)
        
        caminho += f'\\{nomeArquivo}'

        oDataFrame = pandas.DataFrame(linhasExcel)
        oDataFrame.to_excel(caminho, columns = self.columns.get(tipo))

        return caminho