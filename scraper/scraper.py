from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import json

def fetch_product_data_with_selenium(url):
    options = Options()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    driver.get(url)
    time.sleep(10)  # Espera para o carregamento da página
    
    products = []
    product_elements = driver.find_elements(By.CSS_SELECTOR, 'div.s-result-item')

    for product in product_elements:
        try:
            name = product.find_element(By.CSS_SELECTOR, 'span.a-text-normal').text
            price = product.find_element(By.CSS_SELECTOR, 'span.a-price span.a-offscreen').text
            products.append({'name': name, 'price': price})
        except Exception as e:
            print(f"Erro ao extrair dados do produto: {e}")

    driver.quit()
    return products

def save_data_to_json(data, filename='data.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

# Exemplo de uso
url = "https://www.amazon.com.br/s?k=iphone"
filename = 'data.json'  # Definição clara da variável de nome do arquivo
products = fetch_product_data_with_selenium(url)
save_data_to_json(products, filename)
print(f"Dados salvos em {filename}.")  # Uso correto da variável na mensagem de confirmação
