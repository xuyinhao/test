# class person():
#     def setname(self,name1):
#         self.name=name1
#     def getname(self):
#         return self.name
# aa=person()
# aa.setname("aa1")
# print(aa.getname())


class MemberCounter():
    members=0
    def __init__(self):
        MemberCounter.members+=1

m1=MemberCounter()
# print(MemberCounter.members)
m2=MemberCounter()
# print(MemberCounter.members)
# m1=MemberCounter()
# print(MemberCounter.members)
print(m1.members)
print(m2.members)
class MyException(Exception):
    pass
    # while  True:
try:
    x=int(input("x:"))
    y=int(input("y:"))
    a=x/y
    print(a)
except (SystemError,TypeError,NameError,ValueError) as e:
     print("error:",e)
else:
    pass
#     print("finally")
