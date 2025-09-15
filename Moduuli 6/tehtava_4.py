def sum_of_list(luvut):
    summa = 0
    for luku in luvut:
        summa += luku
    return summa

lista = [1, 2, 3, 4, 5]
tulos = sum_of_list(lista)
print(f"The sum of the numbers in the list is: {tulos}")