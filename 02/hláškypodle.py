#  Program podle hlášky ulovené ryby 

ryba = int(input("Zadej váhu své chytěné ryby "))

if ryba >= 200:
    print(ryba,"kg")
    print("Chytil jsi velrybu")
elif ryba >= 100:
    print(ryba,"kg")
    print("Chytil jsi něco opravdu velkého")
elif ryba >= 30:
    print(ryba,"kg")
    print("Mistr ČR")
elif ryba >= 1:
    print(ryba,"kg")
    print("Normalní rybáář")
else:
    print("Neumíš chystat ryby")