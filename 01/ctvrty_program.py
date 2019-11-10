def pozdrav (meno):
    print('Vítam ťa', meno)
    if meno == 'Vendy':
        print ('Ty umíš programovat!')
    print('Ako sa máš?')

pozdrav('Tomas')
pozdrav ('Petra')
pozdrav ('Vendy')

def dvojnasobek (x):
    vysledek = x * 2
    return vysledek


print (dvojnasobek(80))
