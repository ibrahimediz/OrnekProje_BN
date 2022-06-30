class A:
    def __init__(self):
        self.__x = None
    def getx(self):
        print("Getirildi")
        return self.__x
    def setx(self, x):
        if isinstance(x, int):
            if 20 > x >= 0:
                self.__x = x
            else:
                raise ValueError("x değeri 0 ile 20 arasında olmalı")
        print("Değiştirildi")

    def delx(self):
        print("Silindi")
        del self.__x
    x = property(getx, setx, delx, "I'm the 'x' property.")

obj1  = A()
obj1.x = 19 # Değiştirildi
print(obj1.x) # Get edildi 5
# obj1.__x # 'A' object has no attribute '__x'
