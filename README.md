# tarot_cards
This is a python repository with some code that has a lot of properties for each card so its easy to find associations in readings.
https://github.com/ddtraveller/tarot_cards

## Basic Usage
```
# spin up the object
from tarot import TarotCards, Card
t = TarotCards()

# get a random card
card_obj, raw_card_name =  t.rnd_card(played_cards=[])

# there are a number of properties for major and minor arcana cards
# ex: 'astrology', 'card_name', 'card_sephira', 'card_text', 'card_type', 'card_url', 'emotional_score', 'h_letter', 'h_number', 'h_origin', 'h_text', 'neg', 'neu', 'pos', 'tree_location', 'tree_num', 'world'

# print out the card name and a description of the card
print(f'{card_obj.card_name}.title()' is your first card. {{card_obj.card_text})
```
The properties relate to astrology, kabbalah, hebrew letters, emotions and location on the tree of life.
Emotion scores look something like this;
```
emotional_score={'Calm': 0.20, 'Mystical': 0.23, 'Overwhelmed': 0.00, 'Curious': 0.30, 'Happy': 0.22, 'Angry': 0.0, 'Surprised': 0.44, 'Sad': 0.22, 'Fearful': 0.11}, pos='0.749', neu='0.135', neg='0.067',
```
The pos, neg, neu values were derived using AWS comprehension.
The emotions were done with another lib but that one was terrible so I re did them by hand.

Get 6 cards but don't include the fool or magician cards and then count the number of cards that include an angel or a crown and then print the description of the crown if it exists.
```
cards = t.rnd_card_list(6, played_cards=['fool', 'magician'])
for card, c_obj in cards.items():
    if card in t.angels:
        t.angels_count += 1
    if card in t.crowns:
        t.crowns_count += 1
        print(f'This is a description of the crown in the card: {t.crowns_desc_dict[card]}')
```
Get the main emotion of a card;
```
emotions = card_obj.emotional_score
max_emotion = max(zip(emotions.values(), emotions.keys()))[1]
```



