#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[2]:


suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}


# In[3]:


class Card:
    
        def __init__(self,rank,suit):
            self.suit = suit
            self.rank = rank
            self.value = values[rank]
            
        def __str__(self):
            return f'{self.rank} of {self.suit}'


# In[4]:


class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(rank,suit))
    
    def shuffle(self):
        random.shuffle(self.all_cards)
    
    def deal_one(self):
        return self.all_cards.pop(0)
    


# In[23]:


class Player:
    def __init__(self,name):
        self.name = name
        self.all_cards = []
    
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'


# In[51]:





# In[52]:





# In[54]:


#Game setup
player_one = Player('one')
player_two = Player('two')

game_deck = Deck()
game_deck.shuffle()

for x in range(26):
    player_one.add_cards(game_deck.deal_one())
    player_two.add_cards(game_deck.deal_one())
    
game_on = True

#Game logic

round_num = 0

while game_on:
    round_num += 1
    print(f'Round {round_num}')
    
    if len(player_one.all_cards) == 0:
        print('Player one has run out of cards! Player two wins!')
        game_on = False
        break
        
    elif len(player_two.all_cards) == 0:
        print('Player two has run out of cards! Player one wins!')
        game_on = False
        break

    #Start new round
    player_one_cards = []
    player_two_cards = []
    
    player_one_cards.append(player_one.remove_one())
    player_two_cards.append(player_two.remove_one())
    
    at_war = True
    
    while at_war:
        
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False
            
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war = False
            
        else:
            # AT WAR
            print('WAR!')
            
            if len(player_one.all_cards) < 5:
                print('Player one has insufficient cards! Player two wins! Game over at war!')
                game_on = False
                break
            
            elif len(player_two.all_cards) < 5:
                print('Player two has insufficient cards! Player one wins! Game over at war!')
                game_on = False
                break
                
            else:
                for i in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
                
                
            
    
    
    
    
    


# In[ ]:



