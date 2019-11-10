

#  zkusíme něco naprogramovat.
print("Vítá vás super hra jménem kámen, nůžky, papír.")

tah_pocitac = range
3 == "kamen"
2 == "nuzky"
1 == "papir"
tah_cloveka = input("Zadej, kamen, nužky nebo papir: ")
for i in range(1,2,3):   
    if tah_cloveka == "kamen":
        if tah_pocitac == "kamen":
            print("Remíza")
        elif tah_pocitac == "nuzky":
            print("Vyhral jsi")
        elif tah_pocitac == "papir":
            print("Vyhral Počitač")
    if tah_cloveka == "nuzky":
        if tah_pocitac == "nuzky":
            print("Remíza")
        elif tah_pocitac == "papir":
            print("Vyhral jsi")
        elif tah_pocitac == "kamen":
            print("Vyhral Počitač")
    if tah_cloveka == "papir":
        if tah_pocitac == "papir":
            print("Remíza")
        elif tah_pocitac == "kamen":
            print("Vyhral jsi")
        elif tah_pocitac == "nuzky":
            print("Vyhral Počitač")
    else:
        print("Nerozumím")


    