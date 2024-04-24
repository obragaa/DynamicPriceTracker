# DynamicPriceTracker

## Descrição
DynamicPriceTracker é uma ferramenta de scraping web desenvolvida para extrair informações de preços e produtos de sites de e-commerce, como a Amazon. Utiliza Selenium para simular a navegação humana em um navegador, permitindo a captura de dados dinamicamente gerados por JavaScript.

## Funcionalidades
- Extração de nomes e preços de produtos listados em páginas de e-commerce.
- Salva os dados extraídos em formato JSON.
- Capaz de contornar algumas medidas básicas anti-bot através de headers personalizados e tempos de espera.

## Pré-requisitos
Antes de iniciar, certifique-se de ter o seguinte software instalado:
- Python 3.8 ou superior
- Selenium WebDriver
- Chrome ou outro navegador compatível com o driver necessário

## Instalação
Para configurar o ambiente necessário para executar o DynamicPriceTracker, siga os passos abaixo:

1. Clone o repositório para sua máquina local:
   ```
   git clone https://seu-repositorio/DynamicPriceTracker.git

2. Navegue até o diretório do projeto:
    ```
    cd DynamicPriceTracker
    ```

3. Instale as dependências necessárias:

    ```
    pip install -r requirements.txt
    ```
## Uso

Para executar o scraper, use o seguinte comando no terminal:

```
python main.py
```

Isso iniciará o processo de scraping e os dados extraídos serão salvos em data.json no diretório raiz do projeto.


## Configuração

Para modificar a URL de destino ou alterar o comportamento do scraper, edite as variáveis e parâmetros em main.py ou scraper/scraper.py conforme necessário.


## Contribuição

Contribuições são bem-vindas! Se você tem melhorias ou correções, por favor, faça um fork do repositório e envie um pull request, ou abra um issue com os detalhes do seu feedback.


## Licença

Este projeto é distribuído sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
Autores

    Felipe Braga Duarte - Desenvolvimento inicial