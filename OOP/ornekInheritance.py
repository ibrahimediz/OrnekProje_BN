class LandVehicles:
    def __init__(self,marka,motor,yakit,yakitTipi,hibrid=False):
        self.marka = marka
        self.motor = motor
        self.yakit = yakit
        self.yakitTipi = yakitTipi
        self.hibrid = hibrid

    def bilgi(self):
        print("Marka:", self.marka)
        print("Motor:", self.motor)
        print("Yakıt:", self.yakit)
        print("Yakıt Tipi:", self.yakitTipi)
        print("Hibrid:", self.hibrid)

    def yakitAl(self,yakit):
        self.yakit = yakit
        print("Yakıt:", self.yakit)
    
    def motorCalistir(self):
        print(self.marka,self.motor,"Motor çalıştırıldı")
    
class Car(LandVehicles):
    def __init__(self,marka,motor,yakit,yakitTipi,tip):
        super().__init__(marka,motor,yakit,yakitTipi)
        self.tip = tip


class Bus(LandVehicles):
    def __init__(self,marka,motor,yakit,yakitTipi,vip,kapasite):
        super().__init__(marka,motor,yakit,yakitTipi)
        self.vip = vip
        self.kapasite = kapasite

    def bilgi(self): # override
        super().bilgi()
        print("VIP:", self.vip)
        print("Kapasite:", self.kapasite)


    def vipKontrol(self):
        if self.vip == True:
            print("VIP")
        else:
            print("Normal")

class Truck(LandVehicles):
    def __init__(self,marka,motor,yakit,yakitTipi,tip):
        super().__init__(marka,motor,yakit,yakitTipi)
        self.tip = tip


arac1 = Car("BMW","1.6","Dizel","Benzin","Sedan")
arac1.bilgi()
arac2 = Bus("Mercedes","1.6","Dizel","Benzin",True,100)
arac2.bilgi()