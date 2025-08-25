nimi = str(input("Anna nimi: "))
adj = str(input("Anna adjektiivi: "))

print(f"{nimi} oli kävelemässä ulkona koiran kanssa. \n"
      f"{nimi} näki jonkun {adj} vieraan. \n"
      f"Hän oli hämeentynyt ja ei tiennyt mitä tehdä sitten.")

teksti = input(f"Autapa häntä mitä hänen tulee tehdä seuraavaksi. (juosta pois vai tervehtiä) \n")
print(teksti)

if teksti == "juosta pois":
    print(f"{nimi} juoksee pois koiran mukana ja ei koskaan palaa siihen.")
elif teksti == "tervehtiä":
    print(f"{nimi} tutustuu {adj} vieraaseen ja heistä tulee ystäviä.")