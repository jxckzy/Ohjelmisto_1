ika = int(input("Anna ikäsi: "))

# KAIKKI TÄYTYY LAITTAA JÄRJEKSYKSEN MUKAAN (python toimii yläosasta alaspäin)
if ika >= 65:
    print("Olet eläkeiässä.")
elif ika >= 18:
    print("Olet työiässä.")
elif ika >= 7:
    print("Olet koululainen.")
elif ika >= 0:
    print("Olet pikkulapsi.")
else:
    print("Virheellinen ikä.")

# voit samalla rajoittaa muuttuja ettei python virheellisesti panee väärän vastauksen
# esim. if 17 >= ika >= 7
# tai if 65 >= ika >= 18