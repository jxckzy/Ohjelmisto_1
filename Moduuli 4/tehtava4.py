import random

luku = random.randint(1,10)

while True:
    syote = int(input("Guess a number (1-10): "))
    if syote == luku:
        print("Correct")
        break
    elif syote != luku:
        if syote < luku:
            print("Too low")
        elif syote > luku:
            print("Too high")