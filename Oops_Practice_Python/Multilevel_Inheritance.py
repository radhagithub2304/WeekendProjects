class Grandfather:
    def property1(self):
        print("Grandfather property")
class Father(Grandfather):
    def property2(self):
        print("Father property")
class Son(Father):
    def property3(self):
        print("son property")
# obj=Son()
# obj.property3()
# obj.property2()
# obj.property1()
# obj1=Father()
# obj1.property2()
# obj1.property1()
# obj1.property3()AttributeError: 'Father' object has no attribute 'property3'
m1=Grandfather()
m1.property1()

