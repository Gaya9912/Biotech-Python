#single level Inheritence 
# Method1
class Father:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(self.name)
class son(Father):
    def __init__(self,name):
        self.name=name
    def show1(self):
        print(self.name)
x=Father('nagarjuna')
x.show()
y=son('akhil')
y.show1()
y.show()
#method2
class base:
    def __init__(self):
        self._a=32
        print(self._a)
class derived(base):
    def __init__(self):
        base.__init__(self)
        print(self._a+2)
x=base()
y=derived()
print(x._a)
print(y._a)

#Multilevel Inheritence
class base:
    def __init__(self):
        self._a=42
        print(self._a)
class derived(base):
    def __init__(self):
        base.__init__(self)
        print(self._a+2)
class derived1(derived):
    def __init__(self):
        derived.__init__(self)
        print(self._a*2)
x=derived1()

#Multiple Inheritence
class father:
    fathername=''
    def father(self):
        print(self.fathername)
class mother:
    mothername=''
    def mother(self):
        print(self.mothername)
class son1(father,mother):
    son1name=''
    def son1information(self):
        print(self.fathername)
        print(self.mothername)
        print(self.son1name)
s1=son1()
s1.son1name="Prashu"
s1.fathername="Shiva"
s1.mothername="Pavani"
s1.son1information()

#Heirarchial Inheritence
class son1(father,mother):
    son1name=''
    def son1information(self):
        print(self.fathername)
        print(self.mothername)
        print(self.son1name)
class son2(father):
    son2name=''
    def son2information(self):
        print(self.fathername)
        print(self.son2name)
s1=son1()
s1.son1name="Prashu"
s1.fathername="Shiva"
s1.mothername="Pavani"
s1.son1information()
s2=son2()
s2.fathername="Shiva"
s2.son2name="Praveen"
s2.son2information()
s1.Father()