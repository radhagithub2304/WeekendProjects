class Test:
    def __init__(self,name):
        self.name=name
        print(self.name)
    def m1(self):
        del self.name
        print(self.name)
t1=Test("annnu")
t1.m1()
# output:AttributeError: 'Test' object has no attribute 'name' as there is nothing in memory now