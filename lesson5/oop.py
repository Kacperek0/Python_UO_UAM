#!

import random
import names

class Zebra:
    def __init__(self, _imie, _plec, _wiek, _imie_matki = None, _imie_ojca = None):
        self.imie = _imie
        self.plec = _plec
        self.wiek = _wiek
        self.imie_matki = _imie_matki
        self.imie_ojca = _imie_ojca
        
    def __str__(self):
        return("Zebra {}, wiek {}, plec {}, imie matki: {}, imie ojca {}".format(self.imie, self.wiek, self.plec, self.imie_matki, self.imie_ojca))
    
    def __repr__(self):
        return("Zebra {}, wiek {}, plec {}, imie matki: {}, imie ojca {}\n".format(self.imie, self.wiek, self.plec, self.imie_matki, self.imie_ojca))

    cechy_charakterystyczne = None
    przebyte_choroby = None
    ostatnie_sprzatanie = None


    
def krzyzuj(imie1, plec1, wiek1, imie2, plec2, wiek2):
    x = Zebra(imie1, plec1, wiek1)
    y = Zebra(imie2, plec2, wiek2)
    listaZeber = []
    
    if x.plec != y.plec:
        ile = random.randint(1,10)
        i = 0
        while(i < ile):
            if random.choice(["M", "F"]) == "M":
                listaZeber.append(Zebra(_imie = names.get_first_name(gender="male"), _plec = "M", _wiek = 0, _imie_matki = x.imie, _imie_ojca = y.imie))
            else:
                listaZeber.append(Zebra(_imie = names.get_first_name(gender="female"), _plec = "F", _wiek = 0, _imie_matki = x.imie, _imie_ojca = y.imie))

            i += 1
    else:
        print("Nie mozesz skrzyzowac zeber tej samej plci")
        
    print(listaZeber)
    
krzyzuj(names.get_first_name(gender="female"), "K", 10, names.get_first_name(gender="male"), "M", 7)

        