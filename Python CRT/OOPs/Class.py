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


