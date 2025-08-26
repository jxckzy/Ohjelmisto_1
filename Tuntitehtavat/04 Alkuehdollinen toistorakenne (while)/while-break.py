komento = input("Anna komento (\"lopeta\" lopettaa): ")

while komento != "lopeta":
    print("Suoritetaan")
    if komento == "MAYDAY":
        break
    print("Ollaan iffin ulkopuolella, suoritus jatkuu")
    print("Suoritan toiminnon " + komento)

    komento = input("Anna komento: ")

print("Poistuimme while loopista")