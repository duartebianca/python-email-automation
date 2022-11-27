#bibliotecas necessárias
import pandas as pd
from email.message import EmailMessage
import smtplib
import ssl
import os
import mimetypes

#Coloque aqui a senha que você criou no gmail após a autenticação de dois fatores. Para mais informações, consulte o read.me
email_senha = ''

#email de quem esta enviando
email_origem = ''

#Lê a planilha de onde os dados serão extraídos. Basta inserir o nome da planilha desejada dentro das aspas, com a extensão csv.
planilha = pd.read_csv(".csv")

#coletar os dados e colocar numa lista. Entre [''] temos o nome das colunas. Basta trocar para o nome das colunas convenientes a você
emails_de_envio = planilha[''].tolist()
lista_de_nomes = planilha[''].tolist()
feedback = planilha[''].tolist()

#Lembre de trocar o range para acabar na quantidade final de linhas da coluna.
for i in range(0, 78):
  email_destino = emails_de_envio[i]
  nome = lista_de_nomes[i]
  assunto = '' #Campo de assunto do email
  feedback_atual = feedback[i] #uma das colunas no email continha feedbacks.

  #Mensagem que vai no corpo do email. Pode-se usar uma string ou um arquivo.
  corpo = f"Olá, {nome}!\n Insira a mensagem de texto aqui a mais.\n\n" + feedback_atual + "\nMais texto se quiser."

  #cria o email
  mensagem = EmailMessage()
  mensagem["From"] = email_origem
  mensagem["To"] = email_destino
  mensagem["Subject"] = assunto

  #garante a segurança da mensagem
  mensagem.set_content(corpo)
  safe = ssl.create_default_context() 
  
  #parte que realmente envia
  #essa parte do smtplib.SMTP_SSL() terá modificações em seus parâmetros de acorpo com o provedor de email.
  with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = safe) as smtp:
    smtp.login(email_origem, email_senha)
    smtp.sendmail(email_origem, email_destino, mensagem.as_string())
