#一维数据的存储方式主要使用join函数来进行存储
ls=["北京","上海","天津","重庆"]
f=open("city1.csv","w")
f.write(",".join(ls))
f.close()
