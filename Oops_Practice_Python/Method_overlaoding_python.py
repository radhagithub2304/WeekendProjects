class Demo:
    def m1(self):
        print("inside m1")
    def m1(self,value):
        self.value=value
        print("inside m1,value")
    def m1(self,val1,val2):
        self.val1=val1
        self.val2=val2
        print("inside m1 values",val1,val2)
obj=Demo()
obj.m1(10,1)