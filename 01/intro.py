class Kotatko:
    def zamnoukej (self):
          print (self.jmeno,'mňau!')

mourek = Kotatko()
mourek.jmeno = 'Mourek'
mourek.zamnoukej()


micka = Kotatko()
micka.jmeno = 'Micka'
micka.zamnoukej()

print (mourek.jmeno, micka.jmeno)
