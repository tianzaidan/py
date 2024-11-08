#  for  wallpaper  del index.html scripts
#type
'''
  <span style="position: absolute;bottom: 50px;color: white;font-size: 2rem;font-weight: 700;text-shadow: 3px 3px 3px #2f2f2fa8;left: 10px;">
  <script src="http://cmzz.top/tipsjson"></script>
'''

#type 2
'''
change name  js/ad.js
'''

import os
import re

def backup(road_name):
    print("backup start----->",end=' ' )
    bk_name=road_name+'.bak'
    f=open(road_name,'rb')
    f_t=f.read()
    ff=open(bk_name,'wb')
    ff.write(f_t)
    f.close()
    ff.close()
    print(bk_name+"  backup end.",end=' ' )

def get_file_list(file_path):
    dir_list=os.listdir(file_path)
    if not dir_list:
        return
    else:
        #sorted sorted(iterable[,key][,reverse])返回排序后的新序列，不改变原序列
        #reverse 表示正反向，反向：reverse=True
        #lambda
        dir_list=sorted(dir_list,key=lambda x: os.path.getmtime(os.path.join(file_path,x)),reverse=True)
        return dir_list

def replace(reg,reg2,road,num):
    times=0
    dir_list=get_file_list(road)
    for i in dir_list:
        times+=1
        if times == num:
            break
        road_name=road+'\\'+i
        print(road_name,end=' ')
        replace_1(reg,reg2,road_name)

def replace_1(reg,reg2,road_name):
    print("replace start:",end=' ' )
    road_name_1=road_name+r"\index.html"
    if os.path.exists(road_name_1)!=True:
        print(road_name_1+"  not exists")
        return

    print("open file",end=' ' )
    file=open(file=road_name_1,mode="r+",encoding="utf-8")
    file_t=file.read()
    file.close()

    #os.remove(road_name+r"\\index.html.bak")
    
    a=re.search(reg,file_t)
    if a==None:
        print("no match")
        return
    file_t=file_t.replace(a.group(),"")
    b=re.search(reg2,file_t)
    if b==None:
        print("no match")
    
    backup(road_name_1)
    file_t=file_t.replace(b.group(),"")
    file=open(file=road_name_1,mode="w",encoding="utf-8")
    file.write(file_t)
    file.close()
    print("end")
    pass

def del_1(road):#only for: js/ad.js
    for i in os.listdir(road):
        road_name=road+'\\'+i+"\\js"
        print(road_name,end=' ')
        if os.path.exists(road_name+"\\ad.js"):
            os.rename(road_name+"\\ad.js",road_name+"\\ad.js.bak")
            print("change ad.js.bak")
        print("not match")
    pass
    

def main():
    #road_name="E:\\SteamLibrary\\steamapps\\workshop\\content\\431960\\2847863496"
    reg=r"<script.+json.+/script>"
    reg2=r"style.+position:.+px;"

    road=r"F:\SteamLibrary\steamapps\workshop\content\431960"
    replace(reg,reg2,road,15)
    #del_1(road)
    pass

if __name__=='__main__':

    main()
    
