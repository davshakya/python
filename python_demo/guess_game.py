import random

jackpot = random.randint(1, 100)
guess = int(input("Guess karo bhai>>>"))
while guess != jackpot:
    if guess < jackpot:
        print("it is lower")
    else:
        print("It is greater")
    guess = int(input("Dubara Guess karo bhai>>>"))
print("Sahi Jawab")



















