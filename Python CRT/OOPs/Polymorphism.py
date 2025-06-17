class A:
    def __init__(self,a):
        self.a=a
    #Adding two objects
    def __add__(self,o):
        return self.a+o.a
ob1=A(1)
ob2=A(2)
print(ob1+ob2)
ob3=A("Greeks")
ob4=A("For")
print(ob3+ob4)