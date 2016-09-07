import json
import numpy as np
from pprint import pprint

with open('cards.json') as data:
    cards = json.load(data)

print(cards.keys())
pprint(cards['Whispers of the Old Gods'])




