def filter_even_numbers(luvut):
    parilliset_luvut = []
    for luku in luvut:
        if luku % 2 == 0:
            parilliset_luvut.append(luku)
    return parilliset_luvut


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
toinen_lista = filter_even_numbers(lista)
print(f"Original list: {lista}")
print(f"List with even numbers only: {toinen_lista}")