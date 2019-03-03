class A:
    def m1(self):
        print("class A method")
class B(A):
    def m1(self):
        print("class B method")
        super().m1()
class C(B):
    def m1(self):
        print("class c method")
        super().m1()
obj=C()
obj.m1()  hbhbbdc