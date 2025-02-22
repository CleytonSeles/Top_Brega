from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from bs4 import BeautifulSoup
import time

print("Iniciando o script...")

# Configuração do WebDriver do Selenium para Microsoft Edge
options = webdriver.EdgeOptions()
options.add_argument("--headless")  # Para rodar sem abrir o navegador
driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install(), options=options)

print("WebDriver configurado.")

# URL do ranking do Spotify
url = "https://charts.spotify.com/charts/view/regional-global-daily/latest"
driver.get(url)

print("Navegando para o URL do Spotify Charts...")

# Espera para garantir carregamento da página
time.sleep(5)

print("Esperando a página carregar...")

# Captura do HTML da página
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

print("HTML capturado.")

# Fechando o navegador
driver.quit()

print("Navegador fechado.")

# Teste para verificar se o HTML foi capturado corretamente
print(soup.prettify()[:1000])  # Imprime os primeiros 1000 caracteres do HTML

print("Script finalizado.")

