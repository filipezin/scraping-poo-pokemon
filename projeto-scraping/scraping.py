from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
import Pokemon
import pandas as pd


url = 'https://pokemondb.net/pokedex/all'
request = Request(
    url,
    headers = {'User-Agent': 'Chrome'}
)


page = urlopen(request)
page_bytes = page.read()
page_html = page_bytes.decode("utf-8")

sp = soup(page_html, 'html.parser')

pokemon_coluna = sp.find_all('table', id='pokedex')[0].find_all('tbody')[0].find_all('tr')
#0:205
dict_pokemons = {}
for pokemon in pokemon_coluna[0:205]:
    pokemon_data = pokemon.find_all('td')
    nome = pokemon_data[1].find_all('a')[0].getText()
    if pokemon_data[1].find_all('small'):
        nome = pokemon_data[1].find_all('small')[0].getText()
    tipos = []
    for tipo_pokemon in pokemon_data[2].find_all('a'):
        tipos.append(tipo_pokemon.getText())
    dict_pokemons[pokemon_data[0]['data-sort-value']] = {
        'ID' : pokemon_data[0]['data-sort-value'],
        'Nome' : nome,
        'Poder total' : pokemon_data[3].getText(),
        'Vida' : pokemon_data[4].getText(),
        'Ataque' : pokemon_data[5].getText(),
        'Defesa' : pokemon_data[6].getText(),
        'Ataque Especial' : pokemon_data[7].getText(),
        'Defesa Especial' : pokemon_data[8].getText(),
        'Velocidade' : pokemon_data[9].getText(),
        'Tipo' : tipos
    }

lista_objetos = []
for i in range(1,len(dict_pokemons.keys())):
    
    lista_objetos.append(Pokemon.Pokemon(dict_pokemons[str(i)]['ID'],dict_pokemons[str(i)]['Nome'],
                                        dict_pokemons[str(i)]['Poder total'], dict_pokemons[str(i)]['Vida'],
                                        dict_pokemons[str(i)]['Ataque'],dict_pokemons[str(i)]['Defesa'],
                                        dict_pokemons[str(i)]['Ataque Especial'],dict_pokemons[str(i)]['Defesa Especial'],
                                        dict_pokemons[str(i)]['Velocidade'], dict_pokemons[str(i)]['Tipo']))


