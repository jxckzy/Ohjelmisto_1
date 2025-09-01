nimet = []

etunimi = input("Anna ensimmäinen nimi tai lopeta painamalla Enter: ")
while etunimi != "":
    nimet.append(etunimi)
    etunimi = input("Anna seuraava nimi tai lopeta painamalla Enter: ")

for n in nimet:
    print (f"Moi, {n}!")