import ssl
import smtplib
import sqlite3 as sql
import os

from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText


class SOST:
    def __init__(self) -> None:
        self.getEmails()

        self.currentEmail = {
            'subject': None,
            'body': None,
            'attachments': []
        }
    
    def getEmails(self):
        conexao = sql.connect(f'{os.getcwd()}\\db\\database.db')
        cursor  = conexao.cursor()

        dadosBrutos = cursor.execute('SELECT email, senha FROM Emails WHERE tipo = "sender"').fetchall()
        self.sender = {
            'email': dadosBrutos[0][0],
            'senha': dadosBrutos[0][1]
        }

        dadosBrutos = cursor.execute('SELECT email FROM Emails WHERE tipo = "receiver"').fetchall()
        self.receivers = [email[0] for email in dadosBrutos]

        conexao.close()
    
    def setSubject(self, text):
        self.currentEmail['subject'] = text
    
    def setBody(self, text):
        self.currentEmail['body'] = text
    
    def setAttachment(self, filesPaths):
        for filePath in filesPaths:
            with open(filePath, 'rb') as file:
                part = MIMEApplication(
                    file.read(),
                    Name=basename(filePath)
                )
            part['Content-Disposition'] = f'attachment; filename="{basename(filePath)}"'

            self.currentEmail['attachments'].append(part)
        
    
    def buildEmailMessage(self):
        emailMessage = MIMEMultipart()
        emailMessage['From']    = self.sender.get('email')
        emailMessage['To']      = self.receivers[0]
        emailMessage['Subject'] = self.currentEmail.get('subject')
        emailMessage.attach(MIMEText(self.currentEmail.get('body')))

        for attachment in self.currentEmail.get('attachments'):
            emailMessage.attach(attachment)
        
        return emailMessage

    def sendEmail(self):
        emailMessage = self.buildEmailMessage()
        contexto     = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context= contexto) as smtp:
            smtp.login(self.sender.get('email'), self.sender.get('senha'))
            smtp.sendmail(self.sender.get('email'), self.receivers, emailMessage.as_string())

email = SOST()