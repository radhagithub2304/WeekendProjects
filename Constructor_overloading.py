class Test:
      def __init__(self):
        print("in constructor only")
      def __init__(self, val):
        self.val = val
        print("in con", self.val)
obj=Test()
# outputfor:obj=Test()
# TypeError: __init__() missing 1 required positional argument: 'val'