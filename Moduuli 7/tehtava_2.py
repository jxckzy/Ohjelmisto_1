names = set()

while True:
    syöte = input("Anna nimi: ")
    if syöte == "":
        break
    if syöte in names:
        print("Existing name.")
    else:
        print("New name.")
        names.add(syöte)