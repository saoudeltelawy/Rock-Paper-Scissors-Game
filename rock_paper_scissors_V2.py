rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# -------------
# Reference:
# -------------
# 0: Rock
# 1: Paper
# 2: Scissors
# -------------

import random
computer_choice = random.randint(0,2)

user_choice = int(input('Please select 0 for "Rock" and 1 for "Paper" and 2 for "Scissors" \n'))

game_images = [rock, paper, scissors]

print(game_images[user_choice])
print(game_images[computer_choice])


if user_choice == 0:
  if computer_choice == 0:
    # print(rock)
    print(f"You choose Rock and the computer Choose rock so it is a tie!")
  elif computer_choice == 1:
    # print(paper)
    print(f"You choose Rock and the computer Choose paper so you Lose!!!")
  else:
    # print(scissors)
    print(f"You choose Rock and the computer Choose Scissors so you win :D")
elif user_choice == 1:
  print(paper)
  if computer_choice == 0:
    print(f"You choose Paper and the computer Choose rock so you WIN!")
  elif computer_choice == 1:
    print(f"You choose Paper and the computer Choose paper so it is a tie!")
  else:
    print(f"You choose Paper and the computer Choose Scissors so you lose :P")
elif user_choice == 2:
  # print(scissors)
  if computer_choice == 0:
    print(f"You choose Scissors and the computer Choose rock so you lose!")
  elif computer_choice == 1:
    print(f"You choose Scissors and the computer Choose paper so YOU WIN ")
  else:
    print(f"You choose Scissors and the computer Choose Scissors SO IT IS A TIE :P")
else:
  print("You choose a thing which is outside the game 😒")

