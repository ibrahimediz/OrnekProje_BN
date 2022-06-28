class Sinif: # class 
    sinifOzellik = "Sınıf Özelliği" # Sınıf özelliği
    def __init__(self,ornekOzellik): # init metodu (constructor) nesne oluşturulurken çalışır
        # self ile nesne oluşturulurken özellikleri atar
        self.ornekOzellik = ornekOzellik # instance (nesne) attribute (özellik)
        
    
    def ornekMethod(self): #  örnek metodu 
        # eğer bir fonksiyonun parametresi olarak self görürsen bu fonksiyonun örnek metodu olduğunu söylüyor
        print("Sınıf örnek metodu")
        print(self.ornekOzellik)

    @classmethod
    def sinifMethod(cls): # sınıf metodu
        print("Sınıf metodu")
        print(cls.sinifOzellik)


nesne1 = Sinif("1")
nesne2 = Sinif("2")
nesne3 = Sinif("3")
############# Sınıf Özelliği ve methodunun çağırılması #############
# class method and attribute call
print(nesne1.sinifOzellik) # Sınıf Özelliği
print(nesne2.sinifOzellik) # Sınıf Özelliği
print(nesne3.sinifOzellik) # Sınıf Özelliği
print(Sinif.sinifOzellik) # Sınıf Özelliği
nesne1.sinifMethod() # Sınıf metodu
nesne2.sinifMethod() # Sınıf metodu
nesne3.sinifMethod() # Sınıf metodu
Sinif.sinifMethod()  # Sınıf metodu
############# Sınıf Özelliği ve methodunun çağırılması #############
################ Örnek özellik ve metodun çağırılması ##############
# instance method and attribute call
print(nesne1.ornekOzellik) # 1
print(nesne2.ornekOzellik) # 2
print(nesne3.ornekOzellik) # 3
nesne1.ornekMethod() # Sınıf örnek metodu
nesne2.ornekMethod() # Sınıf örnek metodu
nesne3.ornekMethod() # Sınıf örnek metodu
################ Örnek özellik ve metodun çağırılması ##############