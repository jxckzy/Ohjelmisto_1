def gallons_to_liters(gallons):
    return gallons * 3.785

while True:
    gallons = int(input("Enter a volume in American gallons (negative value to quit): "))
    if gallons >= 0:
        litres = gallons_to_liters(gallons)
        print(f"{gallons:.1f} American gallons is {litres:.2f} liters.")
    elif gallons < 0:
        print("Program finished.")
        break