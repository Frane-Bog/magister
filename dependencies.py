import random

#Klasa ostalih funkcija
class misc():
    
    def zamijeni_str(a, b, izuzetak, zamjena_izuterka):
        for i in range(len(b)):
            if b[i] in a:
                a = a.replace(b[i], "")
        for i in range(len(izuzetak)):
            if izuzetak[i] in a:
                a = a.replace(izuzetak[i], zamjena_izuterka[i])
        return a
    
    def radnom_pitanje(koliko_ih_ima, koji_su_obavljeni):
        broj = int()
        broj = random.randint(0,koliko_ih_ima)
        while broj in koji_su_obavljeni:
            broj = random.randint(0,koliko_ih_ima)
        return broj