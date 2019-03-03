class Test:
    def __init__(self,name):
        self.name=name
        print(self.name)
        del self.name
        print(self.name)
t1=Test("kiya")
# output:AttributeError: 'Test' object has no attribute 'name' beacuse there is nothing in memory.I dinnt find anything at all