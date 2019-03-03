class A:
    def __init__(self):
        print("class A constructor")
class B(A):
    def __init__(self):
        print("class B con")
        super().__init__()
class C(B):
    def __init__(self):
        print("class c con")
        super().__init__()

obj=C()
# Super Method:Immediate super method will be executed