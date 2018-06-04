class Rectangle():
    def __init__(self):
        self.width=0
        self.height=0
    def setsize(self,size1):
        self.height,self.width=size1
    def getsize(self):
        return self.width,self.height
    size=property(getsize,setsize)

aa=Rectangle()
aa.setsize((1,2))
print(aa.size)

class CC():

        def getx(self): return self._x
        def setx(self, value): self._x = value
        def delx(self): del self._x
        x = property(getx, setx, delx, "I'm the 'x' property.")

mm=CC()
mm.x="aa"
print(mm.x)
mm1=CC()
mm1.x="a11"
print(mm1.x)
try:
    print(mm.x)
except AttributeError as e:
    print("AttributeError:",e)

class CC2():
    def __init__(self):
        self.x=None
##这些额外函数的名字和 property 下的一样
    @property
    def xx(self):
        """get size"""
        return self.x

    @xx.setter
    def xx(self,value):
        self.x=value

    @xx.deleter
    def xx(self):
        del self.x
m=CC2()
m.xx="m222"
m2=m.xx
print(m2)
del m.xx


class Flight():
    def __init__(self,flight_name):
        self.__status=0
        self.flight_name=flight_name
    # def check_status(self):
    #     return 1

    @property
    def flight_status(self):
        if self.__status == 1:
            print('the flight %s has arrived' %self.flight_name)
        elif self.__status == 0:
            print('the flight %s has cancelled ' %self.flight_name)
        elif self.__status == 2:
            print('the flight %s is flighting' %self.flight_name)
    @flight_status.setter
    def flight_status(self,status):
        self.__status=status

    @flight_status.deleter
    def flight_status(self):
        print("status got removed")
        del self.__status

f=Flight('FA123')
f.flight_status=1
f.flight_status
del f.flight_status
