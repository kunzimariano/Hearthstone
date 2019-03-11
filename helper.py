import os
import json
import numpy as np
from pprint import pprint
from dotenv import load_dotenv


def write_all_cards(data):
    load_dotenv(verbose=True)
    SECRETAPI_TOKEN_KEY = os.getenv("API_TOKEN")
    headers = {
        "X-Mashape-Key": API_TOKEN
    }

    r = requests.get(
        "https://omgvamp-hearthstone-v1.p.mashape.com/cards", headers=headers)

    json_response = r.json()
    with open('all.json', 'w') as outfile:
        json.dump(json_response, outfile, indent=4, sort_keys=True)


def read_all_cards():
    with open('all.json') as data:
        return json.load(data)


def read_standard_cards():
    with open('standard.json') as data:
        return json.load(data)


def write_standard_file(data):
    with open('standard.json', 'w') as outfile:
        json.dump(data, outfile, indent=4, sort_keys=True)


def get_standard_cards(cards):
    standard = []

    sets = ['Basic',
            'Classic',
            "Journey to Un'Goro",
            'Knights of the Frozen Throne',
            'Kobolds & Catacombs',
            'The Witchwood',
            'The Boomsday Project',
            'Rastakhan\'s Rumble']

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
    pprint(card)
    return (card['attack'] + card['health']) / 2


# print(cards.keys())
# generate_standard_file()

# standard = read_standard_cards()

# for card in standard:

#     if card.get('type', '') == 'Minion':
#         card['expectedValue'] = get_expected_value(card)
#         card['value'] = get_minion_value(card)

# pprint(standard)
