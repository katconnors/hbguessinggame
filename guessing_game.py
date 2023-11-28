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
#print(random_number)
guess = None
guess_count = 0
while guess != random_number:
    guess = input("What is your guess?")
    if not("0" in guess or "1" in guess or "2" in guess or "3" in guess or "4" in guess or "5" in guess or "6" in guess or "7" in guess or "8" in guess or "9" in guess):
        print("Not a valid input. Type a number.")
        continue
    else:
        guess = int(guess)
        guess_count +=1
    
    if guess < random_number:
        print(f"{name}, guess is too low.")
    elif guess > random_number:
        print(f"{name}, your guess is too high.")
    elif guess == random_number:
        print(f"{name}, your guess is correct! It took you {guess_count} tries.") 

    
   




