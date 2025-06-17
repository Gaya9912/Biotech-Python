class student:
    def __init__(self,name,rno,mat,phy,che):
        self.name=name
        self.rno=rno
        self.mat=mat
        self.phy=phy
        self.che=che
    def calculation(self):
        if(self.mat>=40 and self.phy>=40 and self.che>=0):
            tot=self.mat+self.phy+self.che
            avg=tot/3
            print(tot)
            print("%.2f"%(avg))
            if(self.mat>40 and self.phy>75) or (self.phy>75 and self.che>75) or (self.che>75 and self.mat>75):
                print("admission is confirmed")
            else:
                print("admission is not confirmed")
        else:
            print("fail")
s1=student("Kiran",501,74,85,85)
s1.calculation()
print()
#Example 2 Method 1
class customer:
    def __init__(self,name,item1,item2,item3,item4):
        self.name=name
        self.item1=item1
        self.item2=item2
        self.item3=item3
        self.item4=item4
    def calculation(self):
        print(self.name)
        total=(self.item1+self.item2+self.item3+self.item4)
        print(total)
        if(total>200):
            tot=total-total*(20/100)
            print(tot)
        else:
            t=total
s1=customer("Gayathri",40,50,110,20)
s1.calculation()
print()
#Method 2
class store:
    def __init__(self,name,noofitems):
        self.name=name
        self.noofitems=noofitems
    def calculation(self):
        x=self.noofitems
        tp=0
        for i in range(x):
            p=int(input())
            tp+=p
        return tp
name=input("Enter the name:")
noofitems=int(input("Enter the noofitems:"))
c1=store(name,noofitems)
tp=c1.calculation()
print("Total:",tp)
if(tp>=200):
    print("After Discount",tp-tp*0.2)
else:
    print(tp)
            
