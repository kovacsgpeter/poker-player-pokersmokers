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
                return 100
        except:
            return 100

    def showdown(self, game_state):
        pass
