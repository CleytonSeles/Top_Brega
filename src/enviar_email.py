import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def enviar_email(destinatario, assunto, corpo, caminho_arquivo):
    remetente = "seu_email"
    senha = "sua_senha"

    # Configuração do e-mail
    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = assunto

    # Corpo do e-mail
    msg.attach(MIMEText(corpo, 'plain'))

    # Anexar o arquivo
    attachment = open(caminho_arquivo, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
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

# Exemplo de uso
enviar_email("destinatario@exemplo.com", "Ranking Billboard Hot 100", "Segue em anexo o ranking da Billboard Hot 100.", "../data/billboard_hot_100.csv")
