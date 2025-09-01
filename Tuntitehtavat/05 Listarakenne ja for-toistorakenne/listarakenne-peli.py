lista = ["Olohuone", "Makuuhuone", "Keittiö", "Parveke", "Vaatehuone", "Kylpyhuone"]
kuvaus = [
    "Olkkarissa vaatekaappi ja tila on valoisa.",
    "Makkarissa sohva ja telkkari",
    "Keittiössä liesi, jääkaappi, kaapit, mikro",
    "Ranskalainen parveke",
    "Vaatehuonetta ei löydy",
    "Kylpparissa sauna ja pyyhkinpesukone"
]

print("Hei ta tervetuloa asuntonäyttöön! Valitse alta olevista huoneista"
      "\nnähdäksesi niiden kuvaus:"
      f"\n1 - {lista[0]}"
      f"\n2 - {lista[1]}"
      f"\n3 - {lista[2]}"
      f"\n4 - {lista[3]}"
      f"\n5 - {lista[4]}"
      f"\n6 - {lista[5]}")
valinta = int(input("Valitse: "))

if valinta == 1:
    print(kuvaus[0])
elif valinta == 2:
    print(kuvaus[1])
elif valinta == 3:
    print(kuvaus[2])
elif valinta == 4:
    print(kuvaus[3])
elif valinta == 5:
    print(kuvaus[4])
elif valinta == 6:
    print(kuvaus[5])
else:
    print("Väärä käyttö")