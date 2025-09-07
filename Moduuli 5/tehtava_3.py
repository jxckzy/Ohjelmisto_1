import math

luku = int(input("Enter an integer: "))

if luku <= 1:
    print(f"{luku} is not a prime number.")
else:
    for i in range(2, int(math.sqrt(luku)) + 1):
        if luku % i == 0:
            print(f"{luku} is not a prime number.")
            break
    else:
        print(f"{luku} is a prime number.")