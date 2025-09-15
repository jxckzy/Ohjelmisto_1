import random

def roll_dice(sivut):
    return random.randint(1, sivut)

while True:
    tahkot = int(input("Give the number of sides: "))
    luku = roll_dice(tahkot)
    print(f"{luku}")
    if luku == tahkot:
        break