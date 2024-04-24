from scraper.scraper import fetch_product_data_with_selenium
from data.storage import save_data_to_json
import json

def main():
    url = 'https://www.amazon.com.br/product/s?k=product'
    filename = 'data.json'  # Definição clara da variável de nome do arquivo
    products = fetch_product_data_with_selenium(url)
    save_data_to_json(products, filename)
    print(f"Dados salvos em {filename}.")  # Uso correto da variável na mensagem de confirmação

def save_data_to_json(data, filename='data.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == '__main__':
    main()
