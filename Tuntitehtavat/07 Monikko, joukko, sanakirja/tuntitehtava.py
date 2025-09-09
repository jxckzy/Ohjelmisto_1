import random

adjektiivit = ("erinomainen", "hyvä", "ihan ok", "surkea")
esineet = ("vesipullo", "tietokone", "kynä")

def inventaario(esineet):
    for e in esineet:
        adj = random.choice(adjektiivit)
        esine = f"{adj} {e}"
        print(esine)
    return

nimi = input("Anna nimi: ")
adj = input("Anna adjektiivi: ")

print(f"{nimi} oli kävelemässä ulkona koiran kanssa. \n"
      f"{nimi} näki jonkun {adj} vieraan. \n"
      f"Hän oli hämeentynyt ja ei tiennyt mitä tehdä sitten.")
print("\nHänellä vaikka on mukana: ")
inventaario(esineet)
print(input("\nKerro mitä hänen on tehtävä seuraavaksi: "))