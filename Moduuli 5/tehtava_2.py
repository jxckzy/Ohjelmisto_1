luvut = []

while True:
    syote = input("Enter a number: ")
    if syote == "":
        break
    luku = int(syote)
    luvut.append(luku)

if luvut:
    luvut.sort(reverse=True)
    top5 = luvut[:5]
    print("The greatest numbers in descending order:")
    for i in top5:
        print(f"{i:.1f}")