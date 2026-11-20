import random

cislo = random.randint(1, 10)

tip = int(input("Hádej číslo od 1 do 10: "))

if tip == cislo:
    print("Správně! Vyhrál jsi!")
else:
    print("Špatně! Správné číslo bylo:", cislo)