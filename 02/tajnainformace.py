#  program který řekne tajemství

from stringcolor import *

informace = input("Zadej tajné heslo: ")
while informace != "Abraka":
    print("Zkus to znovu")
   
    informace = input("Zadej tajné heslo: ")
print(cs("I will be back!","red").bold())

    




    