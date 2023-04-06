#bibliotecas necessárias
import smtplib
import ssl
from email.message import EmailMessage
import os
import mimetypes
import pandas as pd
from jinja2 import Template

#Coloque aqui a senha que você criou no gmail após a autenticação de dois fatores. Para mais informações, consulte o read.me
email_senha = ''

#email de quem está enviando
email_origem = ''

#Lê a planilha de onde os dados serão extraídos. Basta inserir o nome da planilha desejada dentro das aspas, com a extensão csv.
planilha = pd.read_csv("nome_arquivo.csv")

#coletar os dados e colocar numa lista. Entre [''] temos o nome das colunas. Basta trocar para o nome das colunas convenientes a você
emails_de_envio = planilha['E-mail'].tolist()
lista_de_nomes = planilha['Nome'].tolist()
feedback = planilha['Feedback'].tolist()

#Lembre de trocar o range para acabar na quantidade de linhas que você quer.
for i in range(0, 2):
  email_destino = emails_de_envio[i]
  assunto = '' #Campo de assunto do email
  #Mensagem que vai no corpo do email.
  template = Template(open('corpohtml.txt', 'r').read())
  body = template.render(nome=lista_de_nomes[i], feedback_atual = feedback[i])
  
  #cria o email
  mensagem = EmailMessage()
  mensagem["From"] = email_origem
  mensagem["To"] = email_destino
  mensagem["Subject"] = assunto
  
  #garante a segurança da mensagem
  mensagem.set_content(body, subtype='html')
  safe = ssl.create_default_context() 

  #parte que realmente envia
  #essa parte do smtplib.SMTP_SSL() terá modificações em seus parâmetros de acordo com o provedor de email.
  with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = safe) as smtp:
    smtp.login(email_origem, email_senha)
    smtp.sendmail(email_origem, email_destino, mensagem.as_string().encode('utf-8'))
