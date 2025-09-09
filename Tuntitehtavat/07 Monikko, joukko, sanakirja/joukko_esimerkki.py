pelit = {"Monopoli", "Shakki", "Cluedo"} # joukossa ei ole järjestystä, se on järjetön
print(pelit)

pelit.add("Dominion")
print(pelit)

pelit.remove("Shakki")
print(pelit)

pelit.add("Cluedo") # sama alkio voi esiintyä vain kertaalleen, ei voi toistaa samaa
print(pelit)

for p in pelit:
    print(p)

# jos halutaan tyhjä joukko, käytetään funktio set()
nimet = set()
nimet.add("Viivi")
print(nimet)