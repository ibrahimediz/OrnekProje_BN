
class Hero:
    def __init__(self,isim,saldiriGucu,saglik):
        self.isim = isim
        self.saldiriGucu = saldiriGucu
        self.saglik = saglik
    @property
    def saldir(self):
        # print(f"{self.isim} saldırıyor")
        return self.saldiriGucu

    def darbe(self,etki):
        # print(f"{self.isim} savunuyor")  
        self.saglik -= etki

    def saglikDurum(self):
        print(f"{self.isim} sağlık durumu: {self.saglik}")

class MarvelHero(Hero):
    def __init__(self, isim, saldiriGucu, saglik):
        super().__init__(isim, saldiriGucu, saglik)

class DCHero(Hero):
    def __init__(self, isim, saldiriGucu, saglik):
        super().__init__(isim, saldiriGucu, saglik)

class DeadPool(MarvelHero):
    def __init__(self):
        super().__init__("DeadPool", 150, 1000)

class CaptainAmerica(MarvelHero):
    def __init__(self):
        super().__init__("Captain America", 200, 1000)

class IronMan(MarvelHero):
    def __init__(self):
        super().__init__("Iron Man",250,1000)

class Batman(DCHero):
    def __init__(self):
        super().__init__("Batman", 150,1000)

class Superman(DCHero):
    def __init__(self):
        super().__init__("Superman", 200, 1000)

class Flash(DCHero):
    def __init__(self):
        super().__init__("Flash", 250, 1000)

MarvelHeroesList = [DeadPool,CaptainAmerica,IronMan]
DCHeroList = [Batman,Superman,Flash]
import random as rnd
import time
P1 = rnd.choice(MarvelHeroesList)() # random bir MarvelHero seç
P2 = rnd.choice(DCHeroList)() # random bir DCHero seç
print("Seçilen Marver Hero",P1.isim)
print("Seçilen DC Hero",P2.isim)
while P1.saglik > 0 and P2.saglik > 0:
    time.sleep(0.5)
    P2.darbe(P1.saldir)
    P1.darbe(P2.saldir)
    P1.saglikDurum()
    P2.saglikDurum()
else:
    if P1.saglik > P2.saglik:
        print(P1.isim,"Kazandı")
    elif P2.saglik > P1.saglik:
        print(P2.isim,"Kazandı")
    else:
        print("Berabere")