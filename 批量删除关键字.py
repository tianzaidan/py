import os
aa=os.getcwd()
dir_l=os.listdir(aa)
change=input("need delete:") or '新建文本文档'

def ChangeCwd(dir_list):
    dir_a=aa+'\\'
    for i in dir_list:
        temp=dir_a+i
        os.rename(temp,i.replace(change,''))
        #print(temp,os.path.isdir(temp))
    pass

def ChangeCwd_2(dir_list):#two level
    for i in dir_list:
        if os.path.isdir(i):
            ChangeCwd_2(i)
        else:
            temp=dir_a+i
            os.rename(temp,i.replace(change,''))
#ChangeCwd(dir_l)
ChangeCwd_2(dir_l)
