import interfaceAtivos
import interfaceEmail


class Orquestrador:
    def __init__(self) -> None:
        self.interfaceAtivos = interfaceAtivos.Ativos()
        self.interfaceEmail  = interfaceEmail.SOST()
    
    def run(self):
        jsonFii = self.interfaceAtivos.getFii()
        