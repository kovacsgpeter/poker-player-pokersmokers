import json
class Player:
    VERSION = "kuszoPanda"
    own_cards=[]

    def get_own_cards(self, game_state):
        for player in game_state['players']:
            try:
                return player['hole_cards']
            except KeyError:
                pass

    def get_player_bets(self, game_state):
        bets = list()
        for player in game_state['players']:
            try:
                bets.append(player['bet'])
                return bets
            except KeyError:
                pass
            
    def betRequest(self, game_state):

        try:
            returnVal = 0
            own_cards = self.get_own_cards(game_state)
            isPair = Player.check_if_pair(own_cards)
            isHighcard = self.is_highcard(own_cards)
            if isPair or isHighcard:
                returnVal=200



            return returnVal
        except:
            return 657

    def showdown(self, game_state):
        pass

    def check_if_pair(cards):
        if cards[0]['rank']==cards[1]['rank']:
            return True
        else:
            return False

    def is_highcard(cards):
        if cards[0]['rank'] in ["10", "J", "Q", "K", "A"] or cards[1]['rank'] in ["10", "J", "Q", "K", "A"]:
            return True
        else:
            return False










