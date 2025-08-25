# float = liukuluku eli luku desimaalin mukana (2.0, 1.5..)
# integer (int) = tavalliset luvut eli kokonaiset luvut
# string (str) = kaikki luvut tekstinä

fahrenheit_str = input("Anna lämpötila Fahrenheit-asteina: ")
fahrenheit = float(fahrenheit_str)
# float() komento vaihtaa stringistä tai integerista floatiin (tekstistä numeroon)
# int() samalla integeriin (tekstistä numeroon)
# str() toimii samalla stringiin tahtiin (numerosta tekstiin)
celsius = (fahrenheit-32)*5/9

print("Lämpötila Celsius-asteina: " + str(celsius))
print(f"Lämpötila Celsius-asteina: {celsius}")
# molemmalla tavalla voit osoittaa tekstin kirjoittamiseen
# voit muokata numerosta tekstiin str()-komennolla
# voitkin käyttää "f" ja "{muuttaja}" vaihtaksesi tekstiin (f-kirjain sallii sen käyttön)

print(f"Lämpötila Celsius-asteina: {celsius:6.2f}")
# Seuraavassa on esimerkkejä muotoilukoodeista:
# .5f : liukuluku viiden desimaalin tarkkuudella
# 10.2f : liukuluku kahden desimaalin tarkkuudella kymmenen merkkiä leveään kenttään
# <20s : merkkijono 20 merkkiä leveään kenttään vasemman reunan mukaan tasattuna
# 8d : kokonaisluku kahdeksan merkkiä leveään kenttään