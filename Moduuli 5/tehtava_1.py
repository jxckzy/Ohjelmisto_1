import random

n = int(input("How many dice to roll: "))
summa = 0

for i in range(n):
    f = random.randint(1, 6)
    summa += f

print(f"Sum of the dice: {summa}")