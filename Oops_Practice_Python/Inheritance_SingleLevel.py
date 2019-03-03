class Mobile:
    def m1(self):
        print("inside paren class m1")
class Mobilechild(Mobile):
    def m2(self):
        print("inside child class m2")
# obj=Mobilechild()
# obj.m1()
# obj.m2()
obj1=Mobile()
obj1.m1()
obj1.m2()
# //output of obj1.m2()is as below:
# AttributeError: 'Mobile' object has no attribute 'm2'
# Note:Child class can access parent class properties,but parent class cannot acesschild class properties

