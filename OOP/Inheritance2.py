class A:
    def __init__(self):
        self.a = "A"

    def soyle(self):
        print("A Sınıfından çalıştım")

    def soyleA(self):
        print(self.a)


class B:
    def __init__(self):
        self.b = "B"

    def soyle(self):
        print("B Sınıfından çalıştım")

    def soyleB(self):
        print(self.b)


class C(A, B):
    def __init__(self):
        # super().__init__() # A
        A.__init__(self)
        B.__init__(self)
        self.c = "C"

obj1 = C()
obj1.soyle()