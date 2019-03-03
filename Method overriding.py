class A:
    def m1(self):
        print("m1 method in class A")
class B(A):
    def m1(self):
        print("m1 method in class B")
# obj=A()
# obj.m1()
#output of above one is m1 method in class A
obj1=B()
obj1.m1()

#output of above one is m1 method in class B