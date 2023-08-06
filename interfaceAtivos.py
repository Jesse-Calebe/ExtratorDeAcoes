import json
import requests


class Ativos:
    def __init__(self) -> None:
        self.requisicaoFII = {
            'URL_SERVICE': 'https://www.fundsexplorer.com.br/wp-json/funds/v1/get-ranking',
            'HEADERS': {
                'x-funds-nonce': '61495f60b533cc40ad822e054998a3190ea9bca0d94791a1da',
                'Accept': 'application/json, text/plain, */*',
                'Content-Type': 'application/json'
            },
            'PAYLOAD': {}
        }
        self.requisicaoAB  = {
            'URL_SERVICE': None,
            'HEADERS': {},
            'PAYLOAD': {}
        }
        self.requisicaoAE  = {
            'URL_SERVICE': None,
            'HEADERS': {},
            'PAYLOAD': {}
        }
    
    def convertStringToJson(self, text):
        return json.loads(json.loads(text))
    
    def getJson(self, requisicao):
        return self.convertStringToJson(requests.request(
            'GET',
            url     = requisicao.get('URL_SERVICE'),
            headers = requisicao.get('HEADERS'),
            data    = requisicao.get('PAYLOAD'),
            timeout = 60
        ).text)

    def getFii(self):
        return self.getJson(self.requisicaoFII)
        
    def getAcoesBrasileiras(self):
        pass
    
    def getAcoesExtrangeiras(self):
        pass