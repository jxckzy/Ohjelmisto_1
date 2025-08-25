vuosi = int(input("Anna vuosi: "))

if vuosi % 4 == 0 and not vuosi == 2020:
    print("On olympiavuosi.")
elif vuosi == 2021:
    print("Vuosi on poikkeuksellisesti olympiavuosi koronan takia.")
elif vuosi == 2020:
    print("Vuosi ei ole poikkeuksellisesti olympiavuosi.")
else:
    print("Ei ollut olympiavuosi.")