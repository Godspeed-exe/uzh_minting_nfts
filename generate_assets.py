from dotenv import load_dotenv
import random
import os
import json


with open('all_assets.json') as f:
    loaded_assets = json.load(f)
    print(loaded_assets)

number_of_assets = 5

all_assets = []

for i in range (1, number_of_assets+1):

    attack = random.randint(1,70)
    speed = random.randint(1,50)
    defense = random.randint(1,80)
    health = random.randint(1,100)
    type = random.choice(loaded_assets)


    this_type = type['type']
    type_image = type['ipfs']

    new_asset = {"id": i, "type": this_type, "attack": attack, "speed": speed, "defense": defense, "health": health, "ipfs": type_image}

    all_assets.append(new_asset)


with open('assets.json', 'w') as f:
    json.dump(all_assets, f)