from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def obter_titulo(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        titulo = bsObj.body.h1
    except AttributeError as e:
        return None
    return titulo

title = obter_titulo("LINK DO SITE")
if titulo == None:
    print("Titulo não foi encontrada")
else:
    print(title)
