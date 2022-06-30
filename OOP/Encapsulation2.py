class A:
    def __init__(self):
        self.__x = None
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x):
        if isinstance(x, int):
            if 20 > x >= 0:
                self.__x = x
            else:
                raise ValueError("x değeri 0 ile 20 arasında olmalı")
        print("Değiştirildi")
    @x.deleter
    def x(self):
        print("Silindi")
        del self.__x


# __x =>  gizli
# __x_ => gizli
# __x__ => gizli değil
# _x => yarı gizli
