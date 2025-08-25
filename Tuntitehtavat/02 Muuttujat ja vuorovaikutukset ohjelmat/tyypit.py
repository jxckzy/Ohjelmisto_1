# muuttajan tyypit

merkkijono = "string"
numero = 123
boolean = True # aina iso kirjain
boolean2 = False
# virheellinen_boolean = true
lista = [numero, boolean, merkkijono, boolean2] # listaan kirjoitetaan sekä muuttajat että tekstit jne.
monikko = (1.2, 2.3)
sanakirja = {"kissa", "koira"}

arvo = "1"
# toinen = 1 (str ja int ei voida olla yhdessä samassa komentissa (numero ja teksti))
toinen = "1"

print(1 + 1)
print(arvo + toinen)
# jos halutaan laskea yhteen, niin käytetään numerot eli int
# jos halutaan kirjoittaa yhteen, niin käytetään tekstit eli str

eka = -9
toka = 12_456_123_180
toka = 123_567_89
# kun meillä on kaksi samaa muuttajaa, on käytössä vain toinen olemassa oleva muuttaja ekan edessä
kolmas = 4.973
neljäs = -4 + 2j

print(eka)
print(toka)
print(kolmas)
print(neljäs)
print(neljäs.real) # real = reaaliarvot
print(neljäs.imag) # imag = imaginaariarvot