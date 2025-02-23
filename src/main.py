from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import pandas as pd
import os
import time
from datetime import datetime

print("Iniciando o script...")

# Configuração do WebDriver do Selenium para Google Chrome
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Para rodar sem abrir o navegador
driver = webdriver.Chrome(service=webdriver.chrome.service.Service(ChromeDriverManager().install()), options=options)

print("WebDriver configurado.")

# URL do ranking da Billboard Hot 100
url = "https://www.billboard.com/charts/hot-100"
driver.get(url)

print("Navegando para o URL da Billboard Hot 100...")

# Utilizando WebDriverWait para aguardar até que os elementos estejam visíveis
try:
    element_present = EC.presence_of_element_located((By.CLASS_NAME, 'o-chart-results-list-row'))
    WebDriverWait(driver, 30).until(element_present)
except TimeoutException:
    print("Timed out waiting for page to load")
    driver.quit()
    exit()

print("Elementos carregados.")

# Captura do HTML da página
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

print("HTML capturado.")

# Fechando o navegador
driver.quit()

print("Navegador fechado.")

# Extraindo os dados da página
musicas = []
tracks = soup.find_all('li', class_='o-chart-results-list__item')
print(f"Total de músicas encontradas: {len(tracks)}")  # Depuração

for track in tracks:
    try:
        nome_musica = track.find('h3', class_='c-title').text.strip()
        artista = track.find('span', class_='c-label').text.strip()
        musicas.append({"Posição": len(musicas) + 1, "Música": nome_musica, "Artista": artista})
    except AttributeError:
        continue

# Adicionar a data de extração
data_extracao = datetime.now().strftime('%Y-%m-%d')
for musica in musicas:
    musica["Data de Extração"] = data_extracao

print("Dados extraídos:", musicas[:5])  # Exibir os 5 primeiros resultados para confirmar

# Criando DataFrame com Pandas
df = pd.DataFrame(musicas)

# Garantindo que a pasta 'data' existe
if not os.path.exists("../data"):
    os.makedirs("../data")

# Salvando os dados em um arquivo CSV com cabeçalhos claros e índice
df.to_csv("../data/billboard_hot_100.csv", index=False, encoding="utf-8-sig")  # Usando utf-8-sig para evitar problemas de codificação

print("Dados salvos em billboard_hot_100.csv.")






