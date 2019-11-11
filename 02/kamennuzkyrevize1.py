#  Tohle má být revize hry kámen nůžky papír 

print("Vítejte ve hře kámen, nůžky, papír")

tah_cloveka = "kamen"
tah_pc = "nuzky"



if tah_cloveka == tah_pc:
    print("Remiza")
elif tah_cloveka != tah_pc:
    print("Vyhral jsi")
else:
    print("Prohral jsi")
