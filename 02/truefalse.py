# výpočet povrchu a obvodu čtverce 

povrch = int(input("Zadej stranu čtverce pro výpočet povrchu: " ))
objem = int(input("Zadej stranu čtverce pro výpočet objemu: " ))


if povrch >= 1:
    print("Povrch čtverce je", 6 * povrch**2, "cm2")
else:
    print("Zkus to znovu!")
    

if objem >= 1:
    print("Povrch čtverce je", objem**3, "cm3")
else:
    print("Zkus to znovu!")
    

