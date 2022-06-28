class Car:
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



class Bus:
    def __init__(self,marka,motor,yakit,yakitTipi,vip,kapasite,hibrid=False):
        self.marka = marka
        self.motor = motor
        self.yakit = yakit
        self.yakitTipi = yakitTipi
        self.vip = vip
        self.kapasite = kapasite
        self.hibrid = hibrid

    
    def bilgi(self):
        print("Marka:", self.marka)
        print("Motor:", self.motor)
        print("Yakıt:", self.yakit)
        print("Yakıt Tipi:", self.yakitTipi)
        print("VIP:", self.vip)
        print("Kapasite:", self.kapasite)
        print("Hibrid:", self.hibrid)

    def yakitAl(self,yakit):
        self.yakit = yakit
        print("Yakıt:", self.yakit)
    
    def motorCalistir(self):
        print(self.marka,self.motor,"Motor çalıştırıldı")

    def vipKontrol(self):
        if self.vip == True:
            print("VIP")
        else:
            print("Normal")

class Truck:
    def __init__(self,marka,motor,yakit,yakitTipi,tip,hibrid=False):
        self.marka = marka
        self.motor = motor
        self.yakit = yakit
        self.yakitTipi = yakitTipi
        self.tip = tip
        self.hibrid = hibrid
    
    def bilgi(self):
        print("Marka:", self.marka)
        print("Motor:", self.motor)
        print("Yakıt:", self.yakit)
        print("Yakıt Tipi:", self.yakitTipi)
        print("Tip:", self.tip)
        print("Hibrid:", self.hibrid)
    
    def yakitAl(self,yakit):
        self.yakit = yakit
        print("Yakıt:", self.yakit)
    
    def motorCalistir(self):
        print(self.marka,self.motor,"Motor çalıştırıldı")

arac1 = Car("BMW","1.6","Dizel","Benzin")
arac1.bilgi()

arac2 = Bus("Mercedes","1.6","Dizel","Benzin",True,100)
arac2.bilgi()


