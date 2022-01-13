#!/usr/bin/env python
# coding: utf-8

# BLACKJACK:I COULDVE DONE THIS A LOT BETTER TCHTCH. FORGOT I COULDUUSE FUNCTIONS:
# SO FOR NEXT TIME: FIRST DESIGN CLASSES. THEN CREATE LOGIC. NOW LOOK WHICH PARTS OF LOGIC I CAN TURN INTO FUNCTIONS. NOW MAKE FUNCTIONS. THEN DESIGN GAME.
# 
# CLASSES:
# 
# card: suit, rank, values(ace is exception-tuple 1 and 11)
# 
# deck-inherits card: allcards: dealone, shuffle 
# 
# bank: balance: placebet, collectbet
# 
# player: name, allcards: removeone, addcards
# 
# 

# In[1]:


import random
from IPython.display import clear_output


# In[2]:


suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}


# In[3]:


class Card:
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]
    
    def __str__(self):
        return f'{self.rank} of {self.suit}' 
    


# In[4]:


class Deck(Card):
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(rank,suit))
    
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop(0)
    
    def __len__(self):
        return len(self.all_cards)
        


# In[5]:


class Bank:
    def __init__(self, balance):
        self.balance = balance
        
    def place_bet(self, amount):
        self.balance -= amount
    
    def collect_bet(self, amount):
        self.balance += (amount*2)
        
    def __str__(self):
        return f'Balance: {self.balance}$'
    


# In[6]:


class Player:
    def __init__(self):
        
        self.all_cards = []
        self.aces = 0
        self.sum_values = 0
       
    
    def add_card(self, new_card):
        self.all_cards.append(new_card)
        
        
        self.sum_values += new_card.value
        
        if new_card.rank == 'Ace':
            self.aces += 1
            
    def adjust_for_aces(self):
        if self.sum_values > 21 and self.aces:
            self.sum_values -= 10
            self.aces -= 1
            
        
        


# In[7]:


def replay():
    ans= None 
    while ans != 'yes' and ans != 'no':
        ans = input('Do you want to play another round? Yes or no?')
        ans = ans.lower()
    
    if ans == 'yes':
        return True
    else:
        return False


# In[8]:


#GAME SETUP


# In[ ]:


#Game logic

while True:
    
    try:
        balance = int(input('You are playing blackjack! Enter your bank balance: '))
    except:
        print('Invalid number')
        continue
    else:
        break
        
game_deck = Deck()

game_deck.shuffle()
        
player_bank = Bank(balance)
        
game_on = True

round_num = 0

while game_on:
    
    clear_output()
    
    if player_bank.balance == 0:
        print('Out of money!')
        break
        
    round_num +=1
    print(f'Round: {round_num}\n')
    
    while True:
    
        try:
            bet_amount = int(input(f'Place your bet amount from remaining balance! Your balance is: {player_bank.balance}'))
        except:
            print('Invalid number')
            continue
        else:
            if bet_amount > player_bank.balance:
                print('Insufficient balance')
                continue
            else:
                break
       
    player_bank.place_bet(bet_amount)
    print(f'\n{bet_amount}$ bet placed\n')
    
    #GAME SETUP and deal the cards
   


    player = Player()
    dealer = Player()
    
    player.add_card(game_deck.deal_one())
    dealer.add_card(game_deck.deal_one())
    player.add_card(game_deck.deal_one())
    dealer.add_card(game_deck.deal_one())
    player.adjust_for_aces()
    dealer.adjust_for_aces()
    
    
    end = False
    
    # PLAYERS TURN
    
    while True:
        
        
        print('Player cards: \n')
        for card in player.all_cards:
            print(card)
            
        print(f'\nDealer card(1 hidden card): {dealer.all_cards[0]}\n')
        
            
        print(f'Player cards value at: {player.sum_values}\n')
        
        #sumcheck
        
        if player.sum_values == 21:
            print('You win, BLACKJACK!')
            player_bank.collect_bet(bet_amount)
            print(player_bank)
            end = True
            break
            
        elif player.sum_values > 21:
            print('BUST! You lose!')
            print(player_bank)
            end = True
            break
            
        else:
            
            ans= None 
            while ans != 'hit' and ans != 'stand':
                ans = input('Would you like to hit or stand?')
                ans = ans.lower()
            
            if ans == 'stand':
                break
            
            else:
                player.add_card(game_deck.deal_one())
                player.adjust_for_aces()
    
    #DEALERS TURN
    
    while not end:
        
        clear_output()
        
        while dealer.sum_values < 17:
            dealer.add_card(game_deck.deal_one())
            dealer.adjust_for_aces()
        
        print('Dealers cards: ')
        
        for card in dealer.all_cards:
            print(card)
        print(f'\nDealer cards value at: {dealer.sum_values}\n')
        
        if dealer.sum_values > 21:
            print('Dealer BUST! You win!')
            player_bank.collect_bet(bet_amount)
            print(player_bank)
            break
        
        elif dealer.sum_values > player.sum_values:
            print('You lost!')
            print(player_bank)
            break
        
        elif dealer.sum_values < player.sum_values:
            print('You win!')
            player_bank.collect_bet(bet_amount)
            print(player_bank)
            break
        
        else:
            print('DRAW. No money withdrawed')
            player_bank.balance += bet_amount
            print(player_bank)
            break
     
    #REPLAY
    game_on = replay()
        
    
            
            
                
            
            
    
    
    


# In[ ]:




