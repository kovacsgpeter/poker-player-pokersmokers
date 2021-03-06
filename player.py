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
        bets = []
        try:
            for player in game_state['players']:
                bets.append(int(player['bet']))
            print(bets)
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
            has_twopair = self.has_2pairs(own_cards, self.get_community_cards(game_state))
            has_drill = self.has_drill(own_cards, self.get_community_cards(game_state))
            has_full = self.has_full(own_cards, self.get_community_cards(game_state))
            has_hc = self.has_highcard(own_cards)



            if len(self.get_community_cards( game_state))>0:
                if is_pair or has_twopair or has_drill or has_full or is_highcard or has_hc:
                    bet=max(self.get_player_bets(game_state))+1

            else:
                if has_hc and max(self.get_player_bets(game_state)) < 150:
                    bet = max(self.get_player_bets(game_state))

                if is_pair and has_hc:
                    bet = max(self.get_player_bets(game_state)) + 200

            #
                #if is_same_suit or is_highcard:
                    #if max(self.get_player_bets(game_state)) < 300:
                # bet = max(self.get_player_bets(game_state)) + 20
                    #else:
            #bet = 0
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
        if cards[0]['rank'] in ["10", "J", "Q", "K", "A"] and cards[1]['rank'] in ["10", "J", "Q", "K", "A"]:
            return True
        else:
            return False

    def has_highcard(self, cards):
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
        cardv = []
        for card in cards:
            cardv.append( card.values())


        for card in cardv:
            if cardv.count(card)==3 and card in own_cards:
                ret = True
        return ret

    def has_2pairs(self, own_cards, community_cards):
        pairs = 0
        own_cardsv = []
        for card in own_cards:
            own_cardsv.append(card.values())

        comm_cardsv = []
        for card in community_cards:
            comm_cardsv.append(card.values())

        for card in own_cardsv:
            if comm_cardsv.count(card)==2:
                pairs+=1

        if pairs==2:
            return True
        else:
            return False


    def has_full(self, own_cards, community_cards):

        has_full = False

        cards = own_cards + community_cards

        cardv = []
        for card in cards:
            cardv.append(card.values())

        own_cardsv = []
        for card in own_cards:
            own_cardsv.append(card.values())

        comm_cardsv = []
        for card in community_cards:
            comm_cardsv.append(card.values())



        if cardv.count(own_cardsv[0]) == 3 and cardv.count(own_cardsv[1])==2:
            has_full = True
        for card in comm_cardsv:
            if comm_cardsv.count(card) == 3:
                if own_cardsv[1]==own_cardsv[2]:
                    has_full=True





        return has_full



    def all_in(self,game_state):
        for player in game_state['players']:
            if player['name']=="pokerSmokers":
                return int(player['stack'])


