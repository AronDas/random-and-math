import random

randnum = (random.randint(0,9))
print("I have picked a random number between 0 and 9, try and guess it.")

guess = int(input("Enter your guess here:"))

if guess == randnum:
    print("You guessed correct! the number was", randnum)

else:
    print("Wrong the number was:", randnum)