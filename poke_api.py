import requests 
url_base = 'https://pokeapi.co/api/v2/'

#👇INSERT THE POKEMON'S NAME HERE👇
pokemons = ["pikachu", "charmander", "squirtle", "bulbasaur"]

for pokemon in pokemons:
    endpoint = f'{url_base}/pokemon/{pokemon}'
    resposta = requests.get(endpoint)
    pokemon_api = resposta.json() 
    print (f'''
            Nome: {pokemon_api['name']}
            Altura: {pokemon_api['height']}
            Peso: {pokemon_api['weight']}
            ''')

