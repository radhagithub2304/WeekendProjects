class Father:
    def property1(self):
        print("Father has audi car")
class Mother:
    def property2(self):
        print("Mother has red maruti car")
class child(Father,Mother):
    def property3(self):
        print("Child has audi car")
obj=child()
obj.property1()
obj.property2()
obj.property3()
# obj1=Mother()
# obj1.property2()
# obj1.property1()//AttributeError: 'Mother' object has no attribute 'property1'
# m1=Father()
# m1.property1()
# m1.property3()// If we do   "m1.property3()",then we get
# AttributeError: 'Father' object has no attribute 'property3'

