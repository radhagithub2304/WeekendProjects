class Test:
    def m1(self):
        self.eye=2
        self.name="Anu"
    def __init__(self):
        print(self.eye)
        print(self.name)
t1=Test()
t1.m1()
#Output:'Test' object has no attribute