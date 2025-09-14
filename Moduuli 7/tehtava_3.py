def main():
    airports = {}  # Sanakirja ICAO-koodien ja lentokenttien nimien tallentamiseen

    while True:
        print("\nAirport Data Management")
        print("1. Enter a new airport")
        print("2. Fetch airport information")
        print("3. Quit")
        valinta = input("Please choose an option (1-3): ")
        if valinta == "1":
            icao = input("Enter the ICAO code: ").strip().upper()
            nimi = input("Enter the airport name: ").strip()
            airports[icao] = nimi
            print(f"Airport {nimi} with ICAO code {icao} has been added.")
        elif valinta == "2":
            icao = input("Enter the ICAO code: ").strip().upper()
            if icao in airports:
                print(f"The airport with ICAO code {icao} is {airports[icao]}.")
            else:
                print(f"No airport found with ICAO code {icao}.")
        elif valinta == "3":
            print("Thank you for using the Airport Data Management system. Goodbye!")
            break
        else:
            print("Error. Try again.")

main()