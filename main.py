import interfaceAtivos
import interfaceEmail
import interfaceExcel


class Orquestrador:
    def __init__(self) -> None:
        self.interfaceAtivos = interfaceAtivos.Ativos()
        self.interfaceEmail  = interfaceEmail.SOST()
        self.interfaceExcel  = interfaceExcel.GeradorExcel()
        
        self.caminhosArquivos = []
    
    def run(self):
        arquivoFii = self.interfaceExcel.listToExcel(
            'FiiMasterDetail.xlsx',
            self.interfaceAtivos.getFii(),
            'FII'
        )

        self.caminhosArquivos.append(arquivoFii)

        self.enviaEmails()
    
    def enviaEmails(self):
        self.interfaceEmail.setSubject('[BOT Python] Extração de Ativos')
        self.interfaceEmail.setBody('Bom dia.\n\nSegue anexo extração de indicadores de ativos.\n\nAtenciosamento,\nPython Bot')
        self.interfaceEmail.setAttachment(self.caminhosArquivos)

        self.interfaceEmail.sendEmail()
         
         
orq = Orquestrador()
orq.run()