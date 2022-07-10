############### Blackjack Project #####################

############### Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

import random

def deal_card():
  return random.choice(cards)

def calculate_score(cards):
  if sum(cards) == 21:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards[cards.index(11)] = 1
  return sum(cards)

def compare(user_score, computer_score):
  if user_score == computer_score:
    print("Draw!")
  elif computer_score == 0:
    print("You lose!")
  elif user_score == 0:
    print("You win!")
  elif computer_score > 21:
    print("You win!")
  elif user_score > 21:
    print("You lose!")
  else:
    if user_score > computer_score:
      print("You win!")
    else:
      print("You lose!")

def announce(user_cards, user_score, computer_cards, computer_score):
  print(f"Your cards are: {user_cards}")
  print(f"Your score is: {user_score}")
  print(f"The computer cards are: {computer_cards}")
  print(f"The computer score is: {computer_score}")

def game():
  user_cards = []
  computer_cards = []
  
  for n in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  user_score = calculate_score(user_cards)
  computer_score = calculate_score(computer_cards)

  announce(user_cards, user_score, computer_cards, computer_score)

  if user_score == 0:
    print("You win!")
    return
  elif computer_score == 0:
    print("You lose!")
    return
    
  if user_score < 21:
    user_choice = input("Do you want to draw another card? 'y' or 'n' ")
    while user_choice == 'y':
      user_cards.append(deal_card())
      user_score = calculate_score(user_cards)
      announce(user_cards, user_score, computer_cards, computer_score)
      if user_score > 21:
        print("You lose!")
        return
      elif user_score == 0:
        print("You win!")
        return
      user_choice = input("Do you want to draw another card? 'y' or 'n' ")
    else:
      while computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
        announce(user_cards, user_score, computer_cards, computer_score)
        if computer_score == 0:
          print("You lose!")
          return

  compare(user_score, computer_score)
  return

from replit import clear
import art

print(art.logo)
print("Welcome to the game of Blackjack!")

game_choice = input("Do you want to play a game of Blackjack? 'y' or 'n' ")
while game_choice == 'y':
  clear()
  game()
  game_choice = input("Do you want to play another game of Blackjack? 'y' or 'n' ")

print("Have a nice day!")