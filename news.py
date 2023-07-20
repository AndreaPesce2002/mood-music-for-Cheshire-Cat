from cat.mad_hatter.decorators import tool
import feedparser
import json
from bs4 import BeautifulSoup
import requests
import urllib


@tool()
def mood_music(mood, cat):
    """Useful for recommending a song. This tool recommends a song depending on your mood.
     The input is the mood the user demonstrates."""
     
    site="youtube.com"
    ricerca = 'canzoni+' + urllib.parse.quote(mood) + ' site:'+site
    url = 'http://www.google.com/search?q=' + ricerca
    r = requests.get(url)
    testo= r.text
    
    soup = BeautifulSoup(testo, 'html.parser')
    elementi = soup.find_all('a')

    lista_dati = []
    for el in elementi:
        titolo_elemento = el.find('h3')
        if titolo_elemento: 
             titolo = titolo_elemento.text
             link = el['href']
             if site.split('.')[0] in link:
                lista_dati.append({
                    'titolo': titolo,
                    'link': link,
                })

    json_dati_canzoni = json.dumps(lista_dati, ensure_ascii=False, indent=4)
    
    return json_dati_canzoni
