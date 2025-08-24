import random

random_3_digit = ""
for _ in range(3):
    random_3_digit += str(random.randint(0, 9))

random_4_digit = ""
for _ in range(4):
    random_4_digit += str(random.randint(1, 6))

print("3-digit code:", random_3_digit)
print("4-digit code:", random_4_digit)