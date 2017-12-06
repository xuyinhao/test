#字典列子：简单的数据库
people = {
    'Alice':{
        'phone':'1111',
        'addr':'alic_address'
    },
    'Bill':{
        'phone': '2222',
        'addr':'bill_address'
    }
}
#针对电话和地址的标签
labels={
    'phone':'phone number',
    'addr':'address'
}

name=input("Whos name: ")
#查找电话还是地址
request= input("phone(p) or addr(a) ? ")
if request == 'p' : key='phone'
if request == 'a' : key='addr'

if name in people : print("%s's %s is %s" %  \
                          (name,labels[key],people[name][key]))