luvut = []

while True:
    syote = input("Enter a number (or press Enter to quit): ")
    if syote == "":
        break
    else:
        luku = float(syote)
        luvut.append(luku)

if luvut:
    print(f"Smallest number: {min(luvut)}")
    print(f"Largest number: {max(luvut)}")