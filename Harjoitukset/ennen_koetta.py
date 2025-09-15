# tehtävä 1 : if-lause
talviolympialaiset = 2028
if talviolympialaiset == 2028:
    print(f"Talviolympialaiset on vuonna {talviolympialaiset}")
else:
    print("Talviolympialaiset ei ole tänä vuonna")

# tehtävä 2 : while- ja for-lauseet
i = 0
while i < 3:
    print(f"While-lause toimi {i+1} kertaa.") # tuloksena on 0, 1, 2 ennen 3:tta, sillä lisätään +1
    i += 1

for k in range(1,4): # päättyy 4:lla koska se tarvitse +1
    print(f"for-lause toimii {k} kertaa.")

# tehtävä 3 : lista, joukko, monikko ja sanakirja
lista = ["Petri", "Viivi", "Pilvi", "Matti", "Aino"]
lista.pop(0) # TAI lista.remove("Petri")
print(lista, "lista")

monikko = ("Viivi", "Petri", "Matti", "Pilvi", "Aino")
print(monikko, "monikko")

joukko = {"Matti", "Viivi", "Petri", "Aino", "Pilvi"}
joukko.remove("Pilvi") # joukossa esineet ovat JÄRJESTÄMÄTTÖMIÄ ja MUUTTUMATTOMIA !!! unchangeable, unordered

sanakirja = {"Petri":"18",
             "Viivi":"27",
             "Pilvi":"22",
             "Matti":"23",
             "Aino":"25"}
print(f"Petrin ikä on {sanakirja['Petri']}")
print(sanakirja)

# tehtava 4 : funktio
def sanakirja_func():
    for x, y in sanakirja.items():
        print(x,"-", y)

sanakirja_func()