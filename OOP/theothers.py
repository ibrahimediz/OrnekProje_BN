class A:
    def __init__(self,a):
        self.a = a
    
    def __str__(self): # magic function
        return f"A({self.a})"

    def __lt__(self,other): # < operator less than
        return self.a < other.a

    def __gt__(self,other):
        return self.a > other.a
    
    def __eq__(self,other):
        return self.a == other.a
    
    def __le__(self,other):
        return self.a <= other.a
    
    def __ge__(self,other):
        return self.a >= other.a
    
    def __ne__(self,other):
        return self.a != other.a
    
    def __add__(self,other):
        return A(self.a + other.a)

    def __sub__(self,other):
        return A(self.a - other.a)


o1 = A(1)
o2 = A(2)
print(o1<o2)
print(o1)
print(o1+o2)