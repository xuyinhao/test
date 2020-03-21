import fileinput
#通过fileinput进行文件的替换修改
global vdict
vdict = {}
#处理文件，把key,value进行字典存放
#最终返回字典 key
def process(line):
    key = line.split(":")[0]
    value = line.split(":")[1]
    #字典存放，去掉右边的空格
    vdict[str(key).rstrip()] = str(value).rstrip()
    return vdict.keys()
# 传入data2 的line,判断key是否在其中。
#在,则返回这个key
def reset(line):
    for i in vdict:  #字典key
        if  str(i)+"\n" in str(line) or str(i) + " " in str(line):  #可能是空格或者\n
            return i
#获取data文件，并把key,和value进行一一对应
for line in fileinput.input(['data'], mode='r'):
    # print(process(line))
    process(line)
    pass
#读取data2 进行文件的替换.[需要保持data2最后一行有换行符]
for linew in fileinput.input('data2'):    #如果要修改和备份，则加上  , backup='.bak', inplace=1
    #判断这一行是否有需要替换的字符串
    r = reset(linew)
    if r:
        #需要替换则，进行字符替换 key-->value
        nline = linew.rstrip().replace(r,vdict[r])
        print(nline)
    else:
        #不需要替换，则直接打印行即可
        print(str(linew).rstrip())