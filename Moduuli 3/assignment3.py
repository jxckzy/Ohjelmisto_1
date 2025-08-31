sukupuoli = str(input("Enter biological gender (male/female): "))
hemoglobiiniarvo = float(input("Enter hemoglobin value (g/l): "))

if sukupuoli.lower() == "female":
    if 117 <= hemoglobiiniarvo <= 155:
        print("Your hemoglobin is normal.")
    elif 117 > hemoglobiiniarvo:
        print("Your hemoglobin is low.")
    else:
        print("Your hemoglobin is high.")
elif sukupuoli.lower() == "male":
    if 134 <= hemoglobiiniarvo <= 167:
        print("Your hemoglobin is normal.")
    elif 134 > hemoglobiiniarvo:
        print("Your hemoglobin is low.")
    else:
        print("Your hemoglobin is high.")
else:
    print("Invalid gender.")