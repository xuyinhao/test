class FooBar():
    def __init__(self,value=2,m=None,n=None):
        self.value=value
        self.m=8
    # def __del__(self):
    #     print("is del,%s" %self)
class FBB(FooBar):

    def __init__(self):
        super(FBB,self).__init__()
        self.value=9999

a=FooBar(m=3,n=4)
print(a.value)
print(a.m)

b=FBB()
print(b.value)
print(b.m)
#*******************
def checkIndex(key):
    """
    校验 jianzhi
    负数 等
    :param key:
    :return:
    """
    if not isinstance(key,int):raise TypeError
    if key < 0:raise IndexError

class ArithS():
    def __init__(self,start,step):
        """
        sart stop
        补仓
        :param start: 开始计数
        :param step:  步长
        """
        self.start=start
        self.step=step
        self.changed={}

    def __getitem__(self,key):
        checkIndex(key)
        try :return self.changed[key]
        except KeyError:
            return self.start +key*self.step
    def __setitem__(self,key,value):
        """
        修改算术序列中的值
        :param key:
        :param value:
        :return:
        """
        checkIndex(key)
        self.changed[key]=value
    def __len__(self):
        return len(self.changed)

        pass
    def __delitem__(self, key):
        checkIndex(key)
        try:del self.changed[key]
        except (KeyError,IndentationError):print("No Such Key");pass


s=ArithS(1,2)
# s.__setitem__(1,2)
# print(s.__getitem__(4))
print(s[4])
s[4]=44
s[1]=1
s[2]=2

print(s[4])
del s[4]
print(s[4])
print(len(s))
