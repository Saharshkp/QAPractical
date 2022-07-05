from flask import Flask
from flask import request
from application import app
import random as rd 

@app.route('/level', methods=['POST'])
def level():
    level = 0
    data = request.get_json()
    if data['Pokemon'] == 'Moltres':
        level += 99
    if data['Pokemon'] == 'Articuno':
        level += 99   
    if data['Pokemon'] == 'Zapdos':
        level += 99
    if data['Pokemon'] == 'Charizard':
        level += 60
    if data['Pokemon'] == 'Blastoise':
        level += 65
    if data['Pokemon'] == 'Venasaur':
        level += 60
    if data['Pokemon'] == 'Dragonite':
        level += 80
    if data['Pokemon'] == 'Gengar':
        level += 75
    if data['Pokemon'] == 'Rayquaza':
        level += 100
    if data['Pokemon'] == 'Glaceon':
        level += 70
    if data['rarity'] == 'Common':
        level += 25
    if data['rarity'] == 'Uncommon':
        level += 45
    if data['rarity'] == 'Rare':
        level += 75
    if data['rarity'] == 'Legendary':
        level += 100

    return str(level)
    