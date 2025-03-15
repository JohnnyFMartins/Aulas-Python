from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time



# Configurar o Chrome
def configurar_driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_argument("--start-maximized")
    
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    return driver

# Função principal de busca
def buscar_honda_civic():
    driver = configurar_driver()
    try:
        # URL com filtros pré-definidos
        url = "https://www.webmotors.com.br/carros/sp/sao-paulo/honda/civic?ano=2015-&kmate=100000"
        driver.get(url)
        
        # Aguardar carregamento
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div[class^='ContainerCard']"))
        )
        
        # Coletar resultados
        time.sleep(2)
        carros = driver.find_elements(By.CSS_SELECTOR, "div[class^='ContainerCard']")
        
        print("\n🚗 RESULTADOS ENCONTRADOS 🚗\n")
        
        for index, carro in enumerate(carros, 1):
            try:
                titulo = carro.find_element(By.CSS_SELECTOR, "h2").text
                ano_km = carro.find_element(By.CSS_SELECTOR, "div[class*='YearKm']").text
                preco = carro.find_element(By.CSS_SELECTOR, "div[class*='Price']").text
                local = carro.find_element(By.CSS_SELECTOR, "div[class*='Location']").text
                
                print(f" 🔍 CARRO {index}: {titulo}")
                print(f" 📅 Ano/Quilometragem: {ano_km.replace('•', '-')}")
                print(f" 💰 Preço: {preco}")
                print(f" 📍 Localização: {local}")
                print("-" * 50)
                
            except Exception as e:
                print(f"Erro ao ler carro {index}: {str(e)}")
                continue
                
        print(f"\n✅ Busca concluída! {len(carros)} carros encontrados")

    except Exception as e:
        print(f"🚨 Erro durante a busca: {str(e)}")
    finally:
        driver.quit()

# Executar
if __name__ == "__main__":
    buscar_honda_civic()