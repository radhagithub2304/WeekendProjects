class Demo:
    eye=2
    def __init__(self):
        print("inside constructor")
        print(Demo.eye)
    def m1(self):
        print("inside non_static method")
        print(Demo.eye)
        @classmethod
        def m3(cls):
            print("inside class method which is used with decorator")
            print(Demo.eye)
        @staticmethod
        def m4():
            print("inside static method")
            print(Demo.eye)
t1=Demo()
t1.m1()
t1.m3()
t1.m4()