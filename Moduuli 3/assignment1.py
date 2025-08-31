kuha = float(input("Enter the length of the zander in centimeters: "))

if kuha <  42:
    puuttuvat_sentit = round(42 - kuha, 1)
    print("The zander does not meet the size limit.")
    print("Please release the fish back into the lake.")
    print(f"The fish was {puuttuvat_sentit} centimeters below the size limit.")
elif kuha >= 42:
    print("The zander meets the size limit.")