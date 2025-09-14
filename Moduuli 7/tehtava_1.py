def get_season(kuukausi_numero):
    if kuukausi_numero in (12, 1, 2):
        return "winter"
    elif kuukausi_numero in (3, 4, 5):
        return "spring"
    elif kuukausi_numero in (6, 7, 8):
        return "summer"
    elif kuukausi_numero in (9, 10, 11):
        return "autumn"
    else:
        return None


syöte = int(input("Enter the number of a month (1-12): "))
kk = get_season(syöte)
if kk is None:
    print(f"You entered: {syöte}\nPlease enter a number between 1 and 12.")
else:
    print(f"You entered: {syöte}\nThe season is {kk}.")