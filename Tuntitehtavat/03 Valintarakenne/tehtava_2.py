pituus = float(input("Kuinka pitkä olet? "))
ika = int(input("Ikäsi: "))

if 100 < pituus <= 140:
    print("Saa mennä lasten laitteisiin.")
    if pituus == 140 and ika > 8:
        print("Saa mennä tulirekeen myös.")
elif 140 < pituus:
    print("Saa mennä kaikkiin laitteisiin.")
    if pituus < 195:
        print("Saa mennä kirnuunkin.")
else:
    print("Ei saa mennä minnekään.")