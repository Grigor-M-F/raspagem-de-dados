import requests
from bs4 import BeautifulSoup

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
  'Accept-Language': 'en-US,en;q=0.5'
}

def get_detalhes_produto(produto_url: str) -> dict:
    detalhes_produtos = {}

    page = requests.get(produto_url, headers=headers)
    soup = BeautifulSoup(page.content, "lxml")

    try: 

        title_tag = soup.find('span', id= 'productTitle')

        if title_tag and isinstance(title_tag, str) == False:
            title = title_tag.get_text().strip()
        else:
            title = "Título não encontrado"
            
        price_tag = soup.find('span', class_='a-price').get_text().strip()

        if price_tag and isinstance(price_tag, str) == False:
            price = price_tag.get_text().strip()
        else:
            price = "Preço não encontrado"

        detalhes_produtos['title'] = title
        detalhes_produtos['price'] = price
        detalhes_produtos['url'] = produto_url

        return detalhes_produtos

    except Exception as e:
        print("Não é possível buscar detalhes do produtos")
        print(f"Falhou com exceção: {e}")


produto_url = input("Insira a url do produto: ")
detalhes_produto = get_detalhes_produto(produto_url)

print(detalhes_produto)
