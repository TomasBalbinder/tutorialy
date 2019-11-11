#  Tohle má být revize hry kámen nůžky papír 

print("Vítejte ve hře kámen, nůžky, papír")

tah_pc = "kamen"
tah_cloveka = "nuzky"

if tah_cloveka == "kamen" and tah_pc == "kamen" or tah_cloveka == "nuzky" and tah_pc == "nuzky" or tah_cloveka == "papir" and tah_pc == "papir":
    print("Remiza")
elif tah_cloveka == "kamen" and tah_pc == "nuzky" or tah_cloveka == "nuzky" and tah_pc == "papir" or tah_cloveka == "papir" and tah_pc == "kamen":
    print("Vyhral jsi")
else:
    print("Prohral jsi")
