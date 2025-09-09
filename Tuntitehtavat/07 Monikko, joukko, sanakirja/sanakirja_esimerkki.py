numerot = {"Viivi":"050-1234567",
           "Ahmed":"040-1112223",
           "Pekka":"050-7654321"} # sanakirjassa voidaan käyttää kaksoispistettä

numerot["Olga"] = "050-1011012"  # toimii samalla kuin .append()-funktio
numerot["Mary"] = "0401-2132139"

print (numerot)

nimi = input("Anna nimi: ")
if nimi in numerot:
    print (f"Henkilön {nimi} puhelinnumero on {numerot[nimi]}.")