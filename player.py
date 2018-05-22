import json
import random
class Player:
    VERSION = "trymajom"
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
        try:
            bet = 0
            own_cards = self.get_own_cards(game_state)
            print(own_cards)
            is_pair = self.check_if_pair(own_cards)
            is_highcard = self.is_highcard( own_cards)
            is_same_suit = self.if_same_suit_in_hands(own_cards)
            if is_pair or is_highcard:
                if max(self.get_player_bets( game_state))>200:
                    bet= max( self.get_player_bets( game_state))+1
                else:
                    bet=200
            if len(self.get_community_cards( game_state))>0:
                if self.check_if_have_pair_incommunity(own_cards, self.get_community_cards(game_state)):
                    bet=max( self.get_player_bets( game_state))+1

            if is_same_suit:
                if max(self.get_player_bets(game_state)) > 200:
                    bet = max(self.get_player_bets(game_state)) + 20
                else:
                    bet = 500
            print("bet:" + str(bet))
            return bet
        except Exception as e:
            print(e)
            return 444

    def showdown(self, game_state):
        pass

    def check_if_pair(self, cards):
        if cards[0]['rank']==cards[1]['rank']:
            return True
        else:
            return False

    def is_highcard(self, cards):
        if cards[0]['rank'] in ["10", "J", "Q", "K", "A"] or cards[1]['rank'] in ["10", "J", "Q", "K", "A"]:
            return True
        else:
            return False

    def get_community_cards(self, game_state):
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

    def if_same_suit_in_hands(self, cards):
        if cards[0]['suit'] == cards[1]['suit']:
            return True
        else:
            return False

    def has_drill(self, own_cards, community_cards):
        cards = own_cards+community_cards
        ret = False
        for card in cards:
            if cards.count(card)==3 and card in own_cards:
                ret = True
        return ret

    def has_2pairs(self, own_cards, community_cards):
        pairs = 0
        for card in own_cards:
            if community_cards.count(card)==2:
                pairs+=1

        if pairs==2:
            return True
        else:
            return False


    def has_full(self, own_cards, community_cards):
        cards = own_cards + community_cards
        has_full = False

        if cards.count(own_cards[0]) == 3 and cards.count(own_cards[1])==2:
            has_full = True

       



        return has_full





