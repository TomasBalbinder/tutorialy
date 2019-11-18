#Karetni hra Oko bere (blackjack)

from random import randrange 
print("Hraješ karetní hru Oko Bere")
body = 0

while body < 21:
    print("Máš",body,"bodů")
    otazka =("Máš", body , "bodů")
    otazka = input("Chceš další kartu? ")
    if otazka == "ano":
        nahoda = randrange(1,11)
        body = body + nahoda
    elif otazka == "ne":
        print()
        break
    else:
        print("Odpovidej ano nebo ne")


if body == 21:
    print("Vyhral jsi.")
elif body >= 15:
    print("Byl jsi blízko.")
elif body > 21:
    print("Prohral jsi")
print("Tvé score je", body)
print("Děkuji za použití hry.")



        

 