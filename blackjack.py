import time
import random

class Card:
    counter = 0

    def __init__(self, rank, suit, val):
        self.rank = rank
        self.suit = suit
        self.value = val
    

    def __str__(self):
        return (str(self.rank) + " of " + str(self.suit) + " with a value of " + str(self.value))

class Player:
    def __init__(self, name, hand_val, count):
        self.name = name
        self.hv = hand_val
        self.stay = False
        self.hand = []
        self.count = count
    
    def __str__(self):
        return (str(self.name) + "'s current hand value is " + str(self.hv))
    
    def displayHand(self):
    #INPUT: the Player object
    #PROCESS:
    #OUTPUT: the Player object's cards

        return (str(self.hand))

    def update_hand_value(self, value):
    #INPUT: the object being altered and the value of the card dealt
    #PROCESS: if the object's hand value is less than 21 the new value is added to it
    #OUTPUT: the adjusted self.hv object's hand value

        if self.hv < 21:
            self.hv += value
            return self.hv


def main():

    player_1, player_2 = instruction()

    deck = create_deck()

    player1 = Player(player_1, 0, 0)
    player2 = Player(player_2, 0, 0)


    dealer, player = pickPositions(player1, player2)
    players = [dealer, player]

   
    for x in range (2):   
        for player in players:

            if player.stay == False and player.count < 2:
                time.sleep (2)

                deal(player, deck)


    while dealer.hv < 21 and player.hv < 21 and dealer.stay == False and player.stay == False:

        if dealer.count==2 and player.count==2:
            dealerHitOrStay(dealer, deck)

            time.sleep (2)

            hitOrStay(player,deck)

    winner(dealer, player)

def instruction():
#INPUT: players enter their names
#PROCESS: assigns players names to their variable
#OUTPUT: returns player variables

    print('This is a game of blackjack...')
    time.sleep(1)
    print('There will be two players, one will be assigned the role of dealer and the other will be assigned the role of player.')
    print('Both will receive two cards to begin with...')
    time.sleep(1)
    print('From there it will be the choice of each whether they receive another card...')
    print('"Hit" means I will take another card, while "Stay" means I will not take another card.')
    time.sleep(1)
    print('The player with the greater hand value that is no greater than 21 wins the game...')
  
    player_1 = input(str('Player one please enter your name:'))
    player_2 = input(str('Player two please enter your name:'))


    return player_1, player_2

def pickPositions(p1, p2):
#INPUT: player one and player two objects
#PROCESS: randomly assigns each object to the variable title dealer or player
#OUTPUT: the objects with the new variable labels of dealer and player

    positions = [p1 , p2]

    random.shuffle(positions)
    dealer = positions[0]
    print(f'{dealer.name} you will be the dealer')

    time.sleep(1)

    player = positions[1]
    print(f'{player.name} you will be the player')

    return dealer, player

def create_deck():
#INPUT:
#PROCESS: creates card objects while appending each to the deck list
#OUTPUT: deck list that holds all 52 card objects

        deck = []

        suits = ['♠','♥','♣','♦']
        special_values = {'Ace':1, 'King':10, 'Queen':10, 'Jack':10}

        numbers = ['Ace', 'King', 'Queen', 'Jack']

        for i in range(2,11):
            numbers.append(str(i))


        cards = 0
        for suit in suits:
        
            for num in numbers:
                cards += 1
                card = (f'card{cards}')

                # Values 2-10.
                if num.isnumeric(): 
                    card = Card(num, suit, num)
                    deck.append(card)
            
                # Ace, King, Queen, or Jack.
                else: 
                    value = special_values[num]
                    card = Card(num, suit, value)
                    deck.append(card)

        return deck


def deal(player, deck):
#INUPUT: the player that is receiving the card and the deck list holding the 52 card objects
#PROCESS: randomly shuffles list and deals the first one adding it to their hand as well as their hand value
#OUTPUT: prints what the player received as their card and how it appears added to their hand
    
    random.shuffle(deck)
    card = deck[0]

    player.count += 1

    print(f'{player.name} you just got dealt a {card}')

    value = (card.value)

    player.update_hand_value(int(value))

    player.hand.append(str(card.rank) + ' of ' + str(card.suit))

    time.sleep(2)

    print('This is your current hand...')
    print(player.displayHand())


def hitOrStay(player, deck):
#INPUT: the player object and the deck list of 52 card objects as well as the player's decision when input is called for
#PROCESS: depending on how many cards the player has and what their decision is in terms of staying they may be continuously dealt new cards
#OUTPUT: prints "bust" if player has reached 21

    while player.stay == False:
        print(player)

        if player.hv > 21:
            player.stay = True
            print(f'{player.name} declares "bust"')

        else:
            decision = input(f'{player.name} would you like to stay? (y or n)')

            if decision == 'y':
                player.stay = True

            else:
                player.stay = False
                deal(player, deck)
    

def dealerHitOrStay(dealer, deck):
#INPUT: the dealer object and the deck list of 52 card objects
#PROCESS: depending on how many cards the dealer has they may be continuously dealt new cards
#OUTPUT: prints the dealer's play

    while dealer.stay == False:
        print(dealer)

        if dealer.hv <=16:
            dealer.stay = False
            print(f'Dealer (aka {dealer.name}) says "hit"')
            deal(dealer, deck)

        elif dealer.hv > 21:
            dealer.stay = True
            print('Dealer declares "bust"')

        else:
            dealer.stay = True
            print(f'Dealer (aka {dealer.name}) says "stay"')


def winner(dealer, player):
#INPUT: the dealer and player objects
#PROCESS: using their hand value attributes it is determined who the winner of the game is
#OUTPUT: print winner results of game

    if player.hv == 21:
        print(f'Congratulations {player.name} you won with a perfect hand value of 21!')

    elif dealer.hv == 21:
        print(f'Sorry {player.name} ... the dealer won with a perfect hand value of 21')

    elif player.hv < 21 and dealer.hv > 21:
        print(f'Congratulations {player.name} you won!')

    elif dealer.hv < 21 and player.hv > 21:
        print(f'Dang sorry {player.name} you lost')

    elif player.hv < 21 and player.hv > dealer.hv:
        print(f'Congratulations {player.name} you won!')
        print(f'...With a hand value of {player.hv}')

    elif dealer.hv < 21 and player.hv < dealer.hv:
        print(f'Dang sorry {player.name} you lost')
        print(f'You had a hand value of {player.hv} and the dealer had a hand value of {dealer.hv}')

    elif player.hv > 21 and dealer.hv > 21:
        print(f'Sorry {player.name} and {dealer.name} you arere both losers')
        
main()