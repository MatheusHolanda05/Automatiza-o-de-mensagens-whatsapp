import pandas as pd
import urllib3
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from urllib.parse import quote

# Configurando as opções do Chrome para desativar solicitações de permissão
chrome_options = webdriver.ChromeOptions()
prefs = {
    "profile.default_content_setting_values.media_stream_mic": 2, # Desativa solicitações de microfone
    "profile.default_content_setting_values.notifications": 2  # Desativa solicitações de notificações
}
chrome_options.add_experimental_option("prefs", prefs)

# Inicializando o navegador com as opções configuradas
navegador = webdriver.Chrome(options=chrome_options)
navegador.get("https://web.whatsapp.com/")

# Esperando o usuário fazer login no WhatsApp Web
while len(navegador.find_elements(By.ID, "side")) < 1:
    time.sleep(1)

# Inicializando urllib3
http = urllib3.PoolManager()

# Lendo os contatos do arquivo Excel
contatos_df = pd.read_excel("Enviar.xlsx")
print(contatos_df)

# Já estamos com o login feito no WhatsApp Web
for i, mensagem in enumerate(contatos_df["Mensagem"]):
    pessoa = contatos_df.loc[i, "Pessoa"]
    numero = contatos_df.loc[i, "Número"]
    texto = f"Oi {pessoa}! {mensagem}"
    link = f"https://web.whatsapp.com/send?phone={numero}&text={quote(texto)}"

    navegador.get(link)
    while len(navegador.find_elements(By.ID, "side")) < 1:
        time.sleep(1)

    try:
        # Espera até que o campo de mensagem esteja disponível
        time.sleep(10)  # Pequena pausa para garantir que o campo de mensagem esteja carregado
        campo_mensagem = navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div/p/span')
        campo_mensagem.send_keys(Keys.ENTER)
        time.sleep(2)  # Pequena pausa antes de tentar enviar a mensagem
        
        # Localizar e clicar no botão de envio
        botao_envio = navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[2]/button/span')
        botao_envio.click()
        time.sleep(0.5)  # Pequena pausa antes do segundo clique
        botao_envio.click()
        print(f"Enviando mensagem para {pessoa} no número {numero} com o texto: {texto}")
    except Exception as e:
        print(f"Não foi possível enviar mensagem para {pessoa} no número {numero}. Erro: {e}")

    time.sleep(6)  # Espera 6 segundos para cada mensagem ser enviada

navegador.quit()
