import interfaceAtivos
import interfaceEmail
import interfaceExcel
from log import Log


class Orquestrador:
    def __init__(self) -> None:
        self.log = Log()

        self.log.addLog('Orquestrador.__init__ iniciado')
        self.interfaceAtivos = interfaceAtivos.Ativos()
        self.log.addLog('interfaceAtivos ok')
        self.interfaceEmail  = interfaceEmail.SOST()
        self.log.addLog('interfaceEmail ok')
        self.interfaceExcel  = interfaceExcel.GeradorExcel()
        self.log.addLog('interfaceExcel ok')
        
        self.caminhosArquivos = []
    
    def run(self):
        self.log.addLog('Orquestrador.run iniciado')
        arquivoFii = self.interfaceExcel.listToExcel(
            'FiiMasterDetail.xlsx',
            self.interfaceAtivos.getFii(),
            'FII'
        )

        self.caminhosArquivos.append(arquivoFii)

        self.enviaEmails()
        self.log.addLog('Orquestrador.run finalizado')
    
    def enviaEmails(self):
        self.log.addLog('Orquestrador.enviaEmails iniciado')
        self.interfaceEmail.setSubject('[BOT Python] Extração de Ativos')
        self.interfaceEmail.setBody('Bom dia.\n\nSegue anexo extração de indicadores de ativos.\n\nAtenciosamento,\nPython Bot')
        self.interfaceEmail.setAttachment(self.caminhosArquivos)

        self.interfaceEmail.sendEmail()
        self.log.addLog('Orquestrador.enviaEmails finalizado')
         
         
orq = Orquestrador()
orq.run()