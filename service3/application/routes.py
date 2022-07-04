from application import app
import random as rd 

rarities = ["Common", "Uncommon", "Rare", "Legendary"]

@app.route('/rarity', methods=['GET'])
def rarity():
    return rd.choice(rarities)
    
