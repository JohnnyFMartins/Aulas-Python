import requests # Responsavel por enviar a requisição
from bs4 import BeautifulSoup # Reponsável por tratar a requisição

#_class -> feed-post-link

#URL do Site
url = "https://g1.globo.com/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windowns NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTM, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
  
}

# Fazendo requisição HTTP
resposta = requests.get(url, headers=headers)

# verificar se deu tudo certo
if resposta.status_code == 200:
    # códigp 200 -> sucesso
    print("Requisição fita com sucesso.")
    # print(resposta.text) #retorno
    # preenchendo nossa sopa
    soup = BeautifulSoup(resposta.text, "html.parser")
    # encontrando as noticias
    noticias = soup.find_all("a", class_="feed-post-link")

    print("Ultimas noticias do G1:")
    for index, noticia in enumerate(noticias):
        print(f"{index + 1}. {noticia.text.strip()} - {noticia['href']}")
