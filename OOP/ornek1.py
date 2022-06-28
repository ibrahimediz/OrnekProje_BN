class Telefon:
    tip = "İletişim Aracı"
    def __init__(self, marka, model, fiyat):
        self.marka = marka
        self.model = model
        self.fiyat = fiyat
    
    def bilgi(self):
        print("Marka:", self.marka)
        print("Model:", self.model)
        print("Fiyat:", self.fiyat)
        print("Tip:", Telefon.tip)
    
    @classmethod
    def cep(cls):
        print("Cep telefonu")

tlf1 = Telefon("Samsung", "S10", "3000TL")
tlf2 = Telefon("Nokia", "3310", "1000TL")
tlf3 = Telefon("Apple", "Iphone X", "5000TL")
tlf3.bilgi()