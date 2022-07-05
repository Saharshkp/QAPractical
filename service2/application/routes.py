from application import app
import random as rd

Pokemons = ['Moltres','Articuno','Zapdos','Charizard','Blastoise','Venasaur','Dragonite','Gengar','Rayquaza','Glaceon']

@app.route('/Pokemon', methods=['GET'])
def Pokemon():
    return rd.choice(Pokemons)
