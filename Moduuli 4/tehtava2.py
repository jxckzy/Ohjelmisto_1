while True:
    inches = float(input("Enter length in inches (negative value to quit): "))
    if inches < 0:
        print("Program ended.")
        break
    else:
        print(f"{inches} inches is {inches*2.54:.2f} centimeters")