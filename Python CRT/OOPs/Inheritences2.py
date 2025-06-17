#Multilevel
class grandfather:
    def show(self):
        print("this is grandfather class")
class father(grandfather):
    def show1(self):
        print("This is father class")
class son(father):
    def show2(self):
        print("This is son class")
s1=son()
s1.show()
s1.show1()
s1.show2()
print()
#Multiplelevel
class dance:
    def dancing(self):
        print("i can dance")
class fly:
    def flying(self):
        print("i can also fly")
class peacock(dance,fly):
    def sound(self):
        print("I had a good sound")
p1=peacock()
p1.dancing()
p1.flying()
p1.sound()
#Heirarchial
class shape:
    def area(self):
        print("calculate area:")
class circle(shape):
    def circlearea(self,radius):
        print("area of circle",3.14*radius*radius)
class square(shape):
    def squarearea(self,side):
        print("area of square=",side*side)
c1=circle()
c1.area()
c1.circlearea(5)
s1=square()
s1.area()
s1.squarearea(5)
        