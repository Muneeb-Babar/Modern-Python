
import random

print("Welcome to the Snake Game!")
print("Press 'w' for water, 's' for snake, 'g' for gun")

game_val=random.choice([-1,0,1])

user_input = input("Enter Your Choice: ")

game_dict = {'w': 1, 's': -1, 'g': 0}
val=game_dict[user_input]

reverse_game_dict = {1: 'water', -1: 'snake', 0: 'gun'}
print(f"You chose {reverse_game_dict[val]} and other member chose {reverse_game_dict[game_val]}")

if val==0 and game_val==0:
    print("Game Draw")
else:
    if val==1:
        if game_val==0:
            print("You Win")
        elif game_val==-1:
            print("You Lose")
    elif val==-1:
        if game_val==0:
            print("You Lose")
        elif game_val==1:
            print("You Win")
    else:
        print("Invalid Input")

print("Thanks for Playing!")
