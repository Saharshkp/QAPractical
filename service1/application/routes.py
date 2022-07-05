from application import app
from flask import render_template
import requests

@app.route('/')
def index():
    Pokemons = requests.get('http://service2:5000/Pokemon').text
    rarities = requests.get('http://service3:5000/rarity').text
    level = requests.post('http://service4:5000/level',json={'Pokemon':Pokemons,'rarity':rarities})
    return render_template('home.html', Pokemons=Pokemons, Rarity=rarities, level=level.text)