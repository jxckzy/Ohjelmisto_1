import math
# import-komennossa ei voi olla samaa nimeä kuin tiedostteen nimi

# Pii
print(f"{'Pii:':13s}{math.pi:10.5f}")
print(f"Pii: {math.pi:}")
print(f"Pii: {math.pi:.5f}")
print(f"Pii: {math.pi:.100f}")

# Neperin luku (e)
print(f"{'Neperin luku':12s}:{math.e:10.5f}")
print(math.e)
print(f"{math.e:.5f}")
print(f"{math.e:.100f}")