#test
#username_add_get_info

def init(data):
    data['first']={}
    data['second']={}
    data['last']={}

def lookup(data,label,name):
    return data[label].get(name)
    #字典，得到含有这个name key的所有value

def store(data,*fullname):
    for fname in fullname:
        names=fname.split()
        labels=['first','second','last']
        if len(names) == 2 : names.insert(1,'')
        for label,name in zip(labels,names):
            people=lookup(data,label,name)
            if people:
                people.append(fname)
            else:
                data[label][name]=[fname]
storage={}
init(storage)
# store(storage,"徐 银 号")
store(storage,"徐 银 杰","蒋 猪","蒋 狗")
store(storage,"徐 一 号")
store(storage,"徐 一 号")
# store(storage,"二 一 号")
store(storage,"二 银 号")
print(lookup(storage,'first','徐'))
print(storage)


