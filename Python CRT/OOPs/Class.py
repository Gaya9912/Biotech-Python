#Static
class person:
    age=35
p1=person()
print(p1.age)
p2=person()
print(p2.age)
print(person.age)
#Instance method using parameterized Constructor 
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=person('Gaaythri',21)
p2=person('Naveen',24)
print(p1.age,p1.name)
print(p2.age,p2.name)

#Instance without using constructor
class person:
    name=''
    age=''
p1=person()
p1.name='gaythri'
p1.age='21'
p2=person()
p2.name='naveen'
p2.age='24'
print(p1.name,p1.age)
print(p2.name,p2.age)
#Instance method using parameterized Constructor and normal function
class person:
    def __init__(se,name,age):
        se.name=name
        se.age=age
    def printing(self):
        print(self.name,self.age)
    def decide(self):#MajororMinor
        if self.age>18:
            print("Major")
        else:
            print("Minor")
    def convert(self): #uppercaseconversion
        print(self.name.upper())
    def length(self):#Length
        print(len(self.name))
p1=person('Gayathri',15)
p2=person('Naveen',24)
p1.printing()
p2.printing()
p1.decide()
p2.decide()
p1.convert()
p2.convert()
p1.length()
p2.length()
#Non parameterized constructor
class person:
    c=0
    def __init__(self):
        person.c+=1
p1=person()
print(p1.c)
p2=person()
print(person.c)
p3=person()
print(person.c)
#Default constuctor
class student:
    name="Gaya3"
    age="21"
st=student()
print(st.name)
print(st.age)