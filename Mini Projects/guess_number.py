import random

print("Welcome to the Number Guessing Game!")

target=random.randint(1, 100)

while True:
    guess=input("Please enter your guess or Quit(Q): ")

    if guess=="Q":
        break

    guess=int(guess)
    if guess==target:
        print("Congratulations! You've guessed the correct number!")
        break
    elif guess>target:
        print("Your guess is too high. Please try again.")
    else:
        print("Your guess is too low. Please try again.")

print("Thank you for playing the Number Guessing Game!")