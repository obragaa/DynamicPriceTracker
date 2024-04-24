from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def fetch_product_data_with_selenium(url):
    # Configuração do WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    driver.get(url)
    time.sleep(5)  # Espera para o carregamento da página
    
    products = []
    # Localiza elementos pelo XPATH, CSS Selector ou outro método
    product_elements = driver.find_elements(By.CSS_SELECTOR, 'div.s-result-item')
    
    for product in product_elements:
        name = product.find_element(By.CSS_SELECTOR, 'span.a-text-normal').text
        price = product.find_element(By.CSS_SELECTOR, 'span.a-price').text
        products.append({'name': name, 'price': price})
    
    driver.quit()
    return products

# Exemplo de uso
url = "https://www.amazon.com.br/product/s?k=product"
products = fetch_product_data_with_selenium(url)
print(products)
