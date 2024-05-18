from cat.mad_hatter.decorators import tool
import feedparser
import json
from bs4 import BeautifulSoup
import requests
import urllib


@tool()
def mood_music(mood, cat):
    """Questo strumento consiglia una lista di canzone.
     L'input è il tipo di canzone."""
    
    settings = cat.mad_hatter.get_plugin().load_settings()
    site=settings['site']
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
