import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

def enviar_email(destinatario, assunto, corpo, caminho_arquivo):
    remetente = "seu_email@gmail.com"
    senha = "sua_senha"

    # Verificar se o arquivo existe
    if not os.path.isfile(caminho_arquivo):
        print(f"Erro: O arquivo {caminho_arquivo} não foi encontrado.")
        return

    # Configuração do e-mail
    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = assunto

    # Corpo do e-mail
    msg.attach(MIMEText(corpo, 'plain'))

    # Anexar o arquivo
    with open(caminho_arquivo, "rb") as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % os.path.basename(caminho_arquivo))
        msg.attach(part)

    # Configuração do servidor SMTP
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(remetente, senha)

    # Enviar o e-mail
    texto = msg.as_string()
    server.sendmail(remetente, destinatario, texto)
    server.quit()

    print("E-mail enviado com sucesso!")

# Caminho absoluto para o arquivo CSV
caminho_arquivo = os.path.abspath("data/billboard_hot_100.csv")

# Exemplo de uso
enviar_email("destinatario@exemplo.com", "Ranking Billboard Hot 100", "Segue em anexo o ranking da Billboard Hot 100.", caminho_arquivo)
