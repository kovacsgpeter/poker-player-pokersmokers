import json;
class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        gamestat = json.load(game_state);
        if gamestat['pot']>100:
            return 0
        else:
            return 20


    def showdown(self, game_state):
        pass

