class Demo:
    def m1(self):
        print("inside m1")
    def m1(self, name):
        self.name = name
        print("in m1 method",self.name)

    def m1(self, name2, name1):
        self.name2 = name2
        self.name1 = name1
        print("in m1 method",self.name2,self.name1)
obj=Demo()
obj.m1(10)
# output of obj.m1()
# TypeError: m1() missing 2 required positional arguments: 'name2' and 'name1'
#  output of obj.m1():TypeError: m1() missing 1 required positional argument: 'name1'
# output of obj.m1(10,23),:in m1 method 10 23