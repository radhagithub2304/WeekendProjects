class A:
    def __init__(self):
        print("inside old A constructor")
class B(A):
    def  __init__(self):
        print("inside new B constructor")
# obj=A()
obj1=B()