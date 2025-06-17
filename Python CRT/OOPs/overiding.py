class bank:
    def getroi(self):
        return 10
class sbi(bank):
    def getroi(self):
        return 8
class icici(bank):
    def getroi(self):
        return 9
b1=bank()
print(b1.getroi())
s1=sbi()
print(s1.getroi())
i1=icici()
print(i1.getroi())
print()
#Method resolution order
class A:
    def myname(self):
        print("I am a classA")
class B(A):
    def myname(self):
        print("I am a class B")
class C(A):
    def myname(self):
        print("I am a class C")
class D(C,B):
    pass
d=D()
print(D.__mro__)
print(D.mro())
print()
class base:
    def __init__(self):
        self.__a=32
        print(self.__a)
class derived(base):
    def __init__(self):
        base.__init__(self)
        print(self.__a+2)
b1=base()


