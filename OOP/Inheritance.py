class A:
    def __init__(self):
        self.a = "A"

    def soyle(self):
        print("A Sınıfından çalıştım")

    def soyleA(self):
        print(self.a)

class B(A):
    def __init__(self):
        super().__init__()
        self.b = "B"
    


obj1 = B()
obj1.soyle()
obj1.soyleA() 