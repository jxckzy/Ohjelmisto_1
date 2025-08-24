koulu = "Metropolia"
nimi = input('anna nimi: ')
ika = int(input('anna ikä: '))
print(f'Hei {nimi} {ika} vuotta') # virheellinen lainausmerrki hipsu
print(nimi, f', uusi koulusi on {koulu}') # puuttuu muuttajaa 'koulu' ja f-kirjainta
print('Tervetuloa uuteen kouluun!')

uusi_ika = ika + 1
print('Ensi vuonna täytät ' + str(uusi_ika) + ' vuotta') # puuttuu str() kommentoa  tai f-kirjainta
kuukausi = input('Missä kuussa syntymäpäiväsi on?') # 'input'-sanassa on kirjoitusvirhe
print(f'Onnea siis {kuukausi}!') # f-kirjainta puuttuu