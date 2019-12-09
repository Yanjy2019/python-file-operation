import numpy
#Python文件操作大全

#读写操作
f=open("E://Study File-YJY//python学习//a.txt","rb")    #覆盖写操作,其中添加b的后缀主要是为了二进制的形式输出和输入
f1=f.readline()   #只读第一行的内容
print(f1)
f.close()

#在PythonTXT文件的每一行内容前面添加一个“大数据时代”的字符串
f=open("E://Study File-YJY//python学习//a.txt","r+")    #覆盖写操作，读写操作，主要是进行后缀写操作
f1=f.readlines()    #读每一行的内容，并且将其储存为列表的形式
for i in range(len(f1)):
    f1[i]="大数据时代"+f1[i]
print(f1)
f=open("E://Study File-YJY//python学习//a.txt","w+")    #覆盖写操作
f.writelines(f1)
print(f.read())
f.close()

#创建写操作
f=open("E://Study File-YJY//python学习//g3.txt","w+")    #覆盖写操作,如不存则将新建一个文件
f.write("大数据与数据挖掘")
print(f.read())
f.close()

#文件的读写操作
f=open("a.txt","w+")
f.write("床前明月光，疑是地上霜。\n举头望明月，低头思故乡！")
f=open("a.txt","r")
print(f.readline(3))
print(f.read())    #不管是read还是readline函数斗湖都会记录下文件上次读取的地方，继续向下读下去
f.seek(0)    #将文件的指针位置重新返回到w文件的开头位置，重新进行开始读写操作。
print(f.read())
f.close()
#一般文件的写操作
f=open("c.txt","w")
f.write("大数据与数据挖掘技术实现方法介绍\n")
f.write("云计算与物联网技术实现方式")     #在进行文件的写操作时，之所以是覆盖草操作，主要是因为write函数的默认开始指针位置是文件的开始地方，所以为了不断地继续往下添加内容，需要我们自己在每一步操作的后面加一个换行操作，
f.close()
f=f=open("c.txt","r")
print(f.read())
f.close()

#一维数据的存储方式主要使用join函数来进行存储为csv文件或者TXT文件
ls=["北京","上海","天津","重庆"]
f=open("city1.csv","w")
f.write(",".join(ls))    #将一维数据存储为csv文件，逗号分隔值格式
f.close()
#将一维数据的csv文件恢复为list文件
f=open("city1.csv","r")
ls=f.read()
ls_new=ls.split(",")
print(ls_new)    #将存储为csv的文件恢复为list文件
#二维数据的存储和恢复读取操作
ls=[["指标","2014年","2015年","2016年"],
    ["居民消费价格指数","102","101.4","102"]]
f=open("cp.csv","w")
for i in ls:
    f.write(",".join(i)+"\n")
f.close()
f=open("cp.csv","r")
ls=[]
for i in f:
    a=i.strip("\n")
    print(a)
    b=a.split(",")
    print(b)
    ls.append(b)    #集合在一起的形式可以写为ls.append(i.strip("\n").split(","))    #首先将每一行之前所存在的换行操作去掉，之后进行逗号的分割，然后输出为列表像是
f.close()
print(ls)

















