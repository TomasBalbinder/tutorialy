from random import randrange 
tah_cloveka=input("Zadej kamen, nůžky nebo papir: ")
print("Člověk dal:",tah_cloveka)
tah_pocitac = randrange(3)


if tah_pocitac == 0:
    print("Počitač dal nůžky")
elif tah_pocitac == 1:
    print("Počitač dal kamen")
elif tah_pocitac == 2:
    print("Počitač dal papir")

