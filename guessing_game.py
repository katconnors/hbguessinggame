#greet player
#get player name
#choose random number between 1 and 100
#repeat forever:
 #   get guess
  #  if guess is incorrect:
   #     give hint
    #    increase number of guesses
    #else:
     #   congratulate player

#Nadia and Katrina collab
import random

print("Hello and welcome to the Guessing Game!")
name = input("What is your name?")

random_number = random.randint(1,100)
guess = None
guess_count = 7
while guess_count > 0:
    while True:
        try:
            guess = int(input("What is your guess?"))
            break
        except ValueError:
            print("Not a valid input.")

    
    guess_count -=1
    
    if guess < random_number:
        print(f"{name}, guess is too low. You have {guess_count} guesses left.")
    elif guess > random_number:
        print(f"{name}, your guess is too high. You have {guess_count} guesses left.")
    elif guess == random_number:
        print(f"{name}, your guess is correct! It took you {7-guess_count} tries.") 
        break

    
   




