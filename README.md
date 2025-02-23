# 🎵 Top_Brega - Web Scraping e RPA para Spotify
Este projeto automatiza a coleta do ranking de músicas do Spotify via Web Scraping e envia o ranking via e-mail. Utilizamos a página da Billboard Hot 100 como exemplo para demonstrar a funcionalidade.

## 🚀 Tecnologias Utilizadas
Python

Selenium

BeautifulSoup 

Pandas

Git/GitHub
## 📌 Como Rodar o Projeto
### Requisitos
Python 3.6 ou superior

Google Chrome

Conta de e-mail (Gmail) para enviar o ranking
### Instalação
1.Clone este repositório:

sh

    git clone https://github.com/seu_usuario/top_brega.git
    cd top_brega
2.Crie e ative um ambiente virtual:

sh


    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
3.Instale as dependências:

sh


    pip install -r requirements.txt
Uso
1. Executar o Scraper

Para coletar os dados do ranking Billboard Hot 100 e salvar em um arquivo CSV, execute:

sh
 

      python src/main.py
      O arquivo CSV será salvo na pasta data com o nome billboard_hot_100.csv.

2. Enviar o Ranking via E-mail

Para enviar o ranking via e-mail, configure suas credenciais de e-mail no arquivo src/enviar_email.py e execute:

sh


      python src/enviar_email.py
      Configuração do E-mail
      Edite o arquivo src/enviar_email.py com suas credenciais de e-mail:

python


      def enviar_email(destinatario, assunto, corpo, caminho_arquivo):
         remetente = "seu_email@gmail.com"
         senha = "sua_senha"
         ...
#### Estrutura do Projeto

plaintext


      top_brega/
      │
      ├── src/
      │   ├── main.py              # Script principal para coletar dados
      │   ├── enviar_email.py      # Script para enviar e-mail com o ranking
      │
      ├── data/                    # Pasta para armazenar o arquivo CSV gerado
      │
      ├── venv/                    # Ambiente virtual
      │
      ├── .gitignore               # Arquivos e pastas a serem ignorados pelo Git
      ├── README.md                # Documentação do projeto
      ├── requirements.txt         # Lista de dependências do projeto
Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.


Instruções Adicionais:

1.Atualize o arquivo requirements.txt com as dependências necessárias:

plaintext

         beautifulsoup4==4.9.3
         pandas==1.1.3
         selenium==3.141.0
         webdriver-manager==3.2.2

2.Certifique-se de que o arquivo src/enviar_email.py está configurado corretamente com suas credenciais de e-mail.
3.Adicione um .gitignore para ignorar arquivos e pastas desnecessários:

plaintext

         venv/
         __pycache__/
         *.pyc
         *.pyo
         .DS_Store