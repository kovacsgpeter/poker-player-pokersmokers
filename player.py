import json
class Player:
    VERSION = "nem kúszó majom"
    own_cards=[]

    def get_own_cards(self, game_state):
        for player in game_state['players']:
            if player['name']=="pokerSmokers":
                return player['hole_cards']

    def get_player_bets(self, game_state):
        bets = list()
        for player in game_state['players']:
            try:
                bets.append(player['bet'])
                return bets
            except KeyError:
                pass

    def betRequest(self, game_state):

        bet = 0
        own_cards = Player.get_own_cards(game_state)
        print("cards:" +own_cards)
        is_pair = Player.check_if_pair(own_cards)
        print("is_pair:" + is_pair)
        is_highcard = Player.is_highcard(own_cards)
        is_same_suit = Player.if_same_suit_in_hands(own_cards)
        if is_pair or is_highcard:
            if max(Player.get_player_bets(game_state))>200:
                return max( Player.get_player_bets(game_state))+1
            else:
                bet=200
        if len(Player.get_community_cards())>0:
            if Player.check_if_have_pair_incommunity(own_cards, Player.get_community_cards()):
                bet=max( Player.get_player_bets(game_state))+1

        if is_same_suit:
            if max(Player.get_player_bets(game_state)) > 200:
                return max(Player.get_player_bets(game_state)) + 20
            else:
                bet = 500
        print("bet:" + bet)
        return bet

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

    def get_community_cards(game_state):
        cards=[]
        for card in game_state["community_cards"]:
            cards.append(card)
        return cards

    def check_if_have_pair_incommunity(self, own_cards, community_cards):
        for card in own_cards:
            if card in community_cards:
                return True
            else:
                continue
        return False

    def if_same_suit_in_hands(cards):
        if cards[0]['suit'] == cards[1]['self']:
            return True
        else:
            return False



