'''challenge day 4'''
import random

ROCK = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

PAPER = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

SCISSOR = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [ROCK, PAPER, SCISSOR]

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n"))

if player > 2:
  print("You typed an invalid number, you lose!")
else:
  print(options[player])

  random = random.randint(0, 2)
  computer = options[random]
  print(f"computer chose {computer}")

  win = player == 0 and random == 2 or player == 1 and random == 0 or player == 2 and random == 1
  
  lose = player == 0 and random == 1 or player == 1 and random == 2 or player == 2 and random == 0
  
  
  if win == True:
    print("You win")
  elif lose == True:
    print("You Lose")
  else:
    print("Draw")

