# komento = input('Anna komento ("lopeta" lopettaa): ')
# komento = input("Anna komento (\"lopeta\" lopettaa): ")
lopetuskomento = "kissa"
lopetuskomento2 = "lopeta"
lopetuskomento3 = "stop"

kysymys = input("Anna komento (\"lopeta\" lopettaa): ")

while (kysymys != lopetuskomento
       and kysymys != lopetuskomento2
       and kysymys != lopetuskomento3):
    print("hello")
    kysymys = input('Anna komento ("lopeta" lopettaa): ')

print("Poistumme while-rakenteesta")