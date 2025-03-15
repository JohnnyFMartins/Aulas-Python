from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

def configurar_driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--lang=pt-BR")
    
    # Para modo headless (remova o comentário se quiser executar em segundo plano)
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    return driver

def buscar_carros():
    driver = configurar_driver()
    try:
        url = "https://www.webmotors.com.br/carros/estoque?tipoveiculo=carros&anunciante=lojistas|pessoas"
        driver.get(url)
        
        # Aceitar cookies
        try:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "btnCookie"))
            ).click()
        except:
            pass

        # Rolagem para carregar mais veículos
        last_height = driver.execute_script("return document.body.scrollHeight")
        for _ in range(3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(random.uniform(1.0, 2.5))
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        # Coletar dados
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[class*='ContainerCard']"))
        )
        
        cards = driver.find_elements(By.CSS_SELECTOR, "div[class*='ContainerCard']")
        print(f"\n{'-'*40}")
        print(f" 🚗 ENCONTRADOS {len(cards)} CARROS 🚗")
        print(f"{'-'*40}\n")

        for index, card in enumerate(cards, 1):
            try:
                titulo = card.find_element(By.CSS_SELECTOR, "h2[class*='TitleContainer']").text
                ano_km = card.find_element(By.CSS_SELECTOR, "div[class*='YearKmContainer']").text
                preco = card.find_element(By.CSS_SELECTOR, "div[class*='PriceContainer']").text
                local = card.find_element(By.CSS_SELECTOR, "div[class*='LocationContainer']").text
                
                print(f"🔍 VEÍCULO {index}: {titulo}")
                print(f"   📅 Ano/Quilometragem: {ano_km}")
                print(f"   💰 Preço: {preco}")
                print(f"   📍 Localização: {local}")
                print(f"{'-'*40}")

            except Exception as e:
                print(f"Erro ao ler veículo {index}: {str(e)}")
                continue

        print("\n⚠️ Dados coletados do site Webmotors - https://www.webmotors.com.br")

    finally:
        driver.quit()

if __name__ == "__main__":
    print("Iniciando busca... Aguarde!")
    buscar_carros()
    print("Busca concluída!")
