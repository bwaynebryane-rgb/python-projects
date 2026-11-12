import random

print("Welcome to Brian Guessing Game!")

secret = randon.randint(1, 20)
tries = 0

while True:
   guess = int(input("guess a number between 1 and 20: "))
   tries = tries + 1

   if guess == secret:
        print("CORRECT! you got it in", tries, "tries!")
        break
     eliff guess < secret
        print("CORRECT! You got it in", tries, 'tries!")
              break
        elif guess < secret:
            print("Too low! Try higher")
        else
            print("Too high! Try Lower")

  print("Thanks for playing Brian!")
  
