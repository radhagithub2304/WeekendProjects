class Father:
    def property1(self):
        print("father has property")
    def gold(self):
        print("father has gold")
class Mother:
    def property2(self):
        print("Mother has property")
    def gold(self):
        print("Mother has gold")
class child(Mother,Father):
    def property3(self):
        print("child has property")
m1=child()
m1.property3()
m1.property2()
m1.property1()
m1.gold()
# Note:First method of inherited class will execute if both the method names are same