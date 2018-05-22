import json
class Player:
    VERSION = "Default Python folding player"

    def get_own_cards(self, game_state):
        for player in game_state['players']:
            try:
                return player['hole_cards']
            except KeyError:
                pass

    def betRequest(self, game_state):
        try:
            self.own_cards = self.get_own_cards(game_state)

            if game_state['bet'] > 100:
                return 0
            else:
                return 20
        except:
            return 100

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







