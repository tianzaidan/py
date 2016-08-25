import re
import os
import urllib.request
import pprint
import time
s2=r'"objURL":"(http:+?[^\s]+?.jpg|png|gif)"'
#正则表达式！！
#python 中的正则表达式对括号的处理
s2=re.compile(s2)
url=str(input("please input the url:"))
text=urllib.request.urlopen(url).read().decode()
#decode() 转码 缺省值为str    也可以用str转
# read()将http response文件转化问byte文件
# print(text.decode("utf-8")) # 转化以后才可以print
#text.decode("utf-8")
a=""
num=int(input("input the beginning:"))
L=list(re.findall(s2,text))
#pprint.pprint(L)
#pprint的输出也不是严格按照列表来输出的
num-=1
road=input("please input the road:")
road=road+'/'
for a in L:
    time.sleep(1)
    num+=1
    print(num,":",a,"\n")
    f=open(road+str(num)+".jpg","wb")
    try:
        f.write((urllib.request.urlopen(a)).read())
    except:
        num-=1
    finally:
        f.close()
print("we got %d pictures"%num)
print("mission success")
time.sleep(10)
