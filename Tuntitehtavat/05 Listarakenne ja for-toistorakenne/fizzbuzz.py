for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz,")
    elif i % 3 == 0:
        print("fizz,", end=" ")
    elif i % 5 == 0:
        print("buzz,", end=" ")
    else:
        print(str(i)+",", end=" ")