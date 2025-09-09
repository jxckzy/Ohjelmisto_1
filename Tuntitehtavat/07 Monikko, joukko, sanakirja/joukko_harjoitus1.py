esineet = set()

while True:
    syote = input("Anna esine: ")
    if syote == "":
        print(f"Kaikki esineet: {esineet}")
        break
    if syote in esineet:
        print("Löytyy jo, anna jokin muu esine.")
    esineet.add(syote)