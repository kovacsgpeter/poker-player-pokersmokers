import json
class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):


        if game_state['pot']>100:
            return 0
        else:
            return 20


    def showdown(self, game_state):
        pass

    def check_if_pair(self, game_state):
        cards = []

        for item in game_state['players']:
            if item['name']=='pokerSmokers':
                cards = item['hole_cards']

        is_pair=False

        if cards[0]==cards[1]:
            is_pair=True
        if is_pair:
            return cards.values()[0]
        else:
            return False







