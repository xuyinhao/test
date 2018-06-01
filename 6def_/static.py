class MyClass():
    # @staticmethod

    def __init__(self,name):
        self.name=name
    def smeth():
        print("smeth ")
    smeth=staticmethod(smeth)
    @classmethod
    def cmeth(cls):
        print("cmeth",cls)

MyClass.smeth()
MyClass.cmeth()
aa=MyClass("aa")
aa.cmeth()
