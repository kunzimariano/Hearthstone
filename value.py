import json
import numpy as np
from pprint import pprint

def read_all_cards():
    with open('cards.json') as data:
        return json.load(data)

def read_standard_cards():
    with open('standard.json') as data:
        return json.load(data)

def write_standard_file(data):
    with open('standard.json', 'w') as outfile:
        json.dump(data, outfile)

def get_standard_cards(cards):
    standard = []

    sets = ['Basic',
            'Classic',
            'Blackrock Mountain',
            'The Grand Tournament',
            'The League of Explorers',
            'Whispers of the Old Gods',
            'Karazhan']

    for set in sets:
        standard.extend(cards[set])

    return standard

def generate_standard_file():
    cards = read_all_cards()
    standard = get_standard_cards(cards)
    write_standard_file(standard)

def get_expected_value(card):
    return card.get('cost', 0) + 0.5

def get_minion_value(card):
    return (card['attack'] + card['health']) / 2

#print(cards.keys())

standard = read_standard_cards()

for card in standard:
    if card.get('type', '') == 'Minion':
        card['expectedValue'] = get_expected_value(card)
        card['value'] = get_minion_value(card)

print(standard)






