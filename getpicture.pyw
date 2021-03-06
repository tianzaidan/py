#-*- coding:utf-8 -*-
#filename:getpicture.pyw
#create in 2016 7 19
#last improve in 2016 10 2
#change 开多线程 动态加载破解    未完成   待续
#ps:百度图片会有相似图片  但分辨率不同   而且有很多（>50%）过滤出来的地址 403 forbidden
#不足  html js json xml 只针对百度图片 多线程退出问题  子与父关系
#
from tkinter import *   #导入tkinter模块
from tkinter import messagebox #导入messagebox  如果不导入直接运行时会出错 
from tkinter import filedialog #导入filedialog 
from tkinter import simpledialog #导入simpledialog
import threading #导入threaing
import re #导入re
import os #导入os
import os.path #导入os.path
import urllib.request #导入urllib.request
import random #导入random
import pprint #导入pprint

#颜色
colors = '''#FFB6C1 LightPink 浅粉红
#FFC0CB Pink 粉红
#DC143C Crimson 深红/猩红
#FFF0F5 LavenderBlush 淡紫红
#DB7093 PaleVioletRed 弱紫罗兰红
#FF69B4 HotPink 热情的粉红
#FF1493 DeepPink 深粉红
#C71585 MediumVioletRed 中紫罗兰红
#DA70D6 Orchid 暗紫色/兰花紫
#D8BFD8 Thistle 蓟色
#DDA0DD Plum 洋李色/李子紫
#EE82EE Violet 紫罗兰
#FF00FF Magenta 洋红/玫瑰红
#FF00FF Fuchsia 紫红/灯笼海棠
#8B008B DarkMagenta 深洋红
#800080 Purple 紫色
#BA55D3 MediumOrchid 中兰花紫
#9400D3 DarkViolet 暗紫罗兰
#9932CC DarkOrchid 暗兰花紫
#4B0082 Indigo 靛青/紫兰色
#8A2BE2 BlueViolet 蓝紫罗兰
#9370DB MediumPurple 中紫色
#7B68EE MediumSlateBlue 中暗蓝色/中板岩蓝
#6A5ACD SlateBlue 石蓝色/板岩蓝
#483D8B DarkSlateBlue 暗灰蓝色/暗板岩蓝
#E6E6FA Lavender 淡紫色/熏衣草淡紫
#F8F8FF GhostWhite 幽灵白
#0000FF Blue 纯蓝
#0000CD MediumBlue 中蓝色
#191970 MidnightBlue 午夜蓝
#00008B DarkBlue 暗蓝色
#000080 Navy 海军蓝
#4169E1 RoyalBlue 皇家蓝/宝蓝
#6495ED CornflowerBlue 矢车菊蓝
#B0C4DE LightSteelBlue 亮钢蓝
#778899 LightSlateGray 亮蓝灰/亮石板灰
#708090 SlateGray 灰石色/石板灰
#1E90FF DodgerBlue 闪兰色/道奇蓝
#F0F8FF AliceBlue 爱丽丝蓝
#4682B4 SteelBlue 钢蓝/铁青
#87CEFA LightSkyBlue 亮天蓝色
#87CEEB SkyBlue 天蓝色
#00BFFF DeepSkyBlue 深天蓝
#ADD8E6 LightBlue 亮蓝
#B0E0E6 PowderBlue 粉蓝色/火药青
#5F9EA0 CadetBlue 军兰色/军服蓝
#F0FFFF Azure 蔚蓝色
#E0FFFF LightCyan 淡青色
#AFEEEE PaleTurquoise 弱绿宝石
#00FFFF Cyan 青色
#00FFFF Aqua 浅绿色/水色
#00CED1 DarkTurquoise 暗绿宝石
#2F4F4F DarkSlateGray 暗瓦灰色/暗石板灰
#008B8B DarkCyan 暗青色
#008080 Teal 水鸭色
#48D1CC MediumTurquoise 中绿宝石
#20B2AA LightSeaGreen 浅海洋绿
#40E0D0 Turquoise 绿宝石
#7FFFD4 Aquamarine 宝石碧绿
#66CDAA MediumAquamarine 中宝石碧绿
#00FA9A MediumSpringGreen 中春绿色
#F5FFFA MintCream 薄荷奶油
#00FF7F SpringGreen 春绿色
#3CB371 MediumSeaGreen 中海洋绿
#2E8B57 SeaGreen 海洋绿
#F0FFF0 Honeydew 蜜色/蜜瓜色
#90EE90 LightGreen 淡绿色
#98FB98 PaleGreen 弱绿色
#8FBC8F DarkSeaGreen 暗海洋绿
#32CD32 LimeGreen 闪光深绿
#00FF00 Lime 闪光绿
#228B22 ForestGreen 森林绿
#008000 Green 纯绿
#006400 DarkGreen 暗绿色
#7FFF00 Chartreuse 黄绿色/查特酒绿
#7CFC00 LawnGreen 草绿色/草坪绿
#ADFF2F GreenYellow 绿黄色
#556B2F DarkOliveGreen 暗橄榄绿
#9ACD32 YellowGreen 黄绿色
#6B8E23 OliveDrab 橄榄褐色
#F5F5DC Beige 米色/灰棕色
#FAFAD2 LightGoldenrodYellow 亮菊黄
#FFFFF0 Ivory 象牙色
#FFFFE0 LightYellow 浅黄色
#FFFF00 Yellow 纯黄
#808000 Olive 橄榄
#BDB76B DarkKhaki 暗黄褐色/深卡叽布
#FFFACD LemonChiffon 柠檬绸
#EEE8AA PaleGoldenrod 灰菊黄/苍麒麟色
#F0E68C Khaki 黄褐色/卡叽布
#FFD700 Gold 金色
#FFF8DC Cornsilk 玉米丝色
#DAA520 Goldenrod 金菊黄
#B8860B DarkGoldenrod 暗金菊黄
#FFFAF0 FloralWhite 花的白色
#FDF5E6 OldLace 老花色/旧蕾丝
#F5DEB3 Wheat 浅黄色/小麦色
#FFE4B5 Moccasin 鹿皮色/鹿皮靴
#FFA500 Orange 橙色
#FFEFD5 PapayaWhip 番木色/番木瓜
#FFEBCD BlanchedAlmond 白杏色
#FFDEAD NavajoWhite 纳瓦白/土著白
#FAEBD7 AntiqueWhite 古董白
#D2B48C Tan 茶色
#DEB887 BurlyWood 硬木色
#FFE4C4 Bisque 陶坯黄
#FF8C00 DarkOrange 深橙色
#FAF0E6 Linen 亚麻布
#CD853F Peru 秘鲁色
#FFDAB9 PeachPuff 桃肉色
#F4A460 SandyBrown 沙棕色
#D2691E Chocolate 巧克力色
#8B4513 SaddleBrown 重褐色/马鞍棕色
#FFF5EE Seashell 海贝壳
#A0522D Sienna 黄土赭色
#FFA07A LightSalmon 浅鲑鱼肉色
#FF7F50 Coral 珊瑚
#FF4500 OrangeRed 橙红色
#E9967A DarkSalmon 深鲜肉/鲑鱼色
#FF6347 Tomato 番茄红
#FFE4E1 MistyRose 浅玫瑰色/薄雾玫瑰
#FA8072 Salmon 鲜肉/鲑鱼色
#FFFAFA Snow 雪白色
#F08080 LightCoral 淡珊瑚色
#BC8F8F RosyBrown 玫瑰棕色
#CD5C5C IndianRed 印度红
#FF0000 Red 纯红
#A52A2A Brown 棕色
#B22222 FireBrick 火砖色/耐火砖
#8B0000 DarkRed 深红色
#800000 Maroon 栗色
#FFFFFF White 纯白
#F5F5F5 WhiteSmoke 白烟
#DCDCDC Gainsboro 淡灰色
#D3D3D3 LightGrey 浅灰色
#C0C0C0 Silver 银灰色
#A9A9A9 DarkGray 深灰色
#808080 Gray 灰色
#696969 DimGray 暗淡灰
#000000 Black 纯黑'''

panding = 0 #用于判定程序运行与否
tmp = colors.split('\n')          #颜色分离
color = []
for i in tmp:
    j = i.split(' ')
    color.append(j[1])

urlFRAME="http://"
roadFRAME="格式是  X://XXXX//"
def Quit():
    i=messagebox.askquestion('确认','确认退出？')
    if i=='yes':
        root.destroy()
    if i=='no': 
        pass

def get_baiduimage(url,num):
    json = {}
    addresslist = []
    urlsplit = url.split("&")
    for i in urlsplit:
        search = i.split("=")
        json[search[0]] = search[1]
    word = json['word']
    #获取word后面的值  也就是搜索的东西的“不知道编码”的编码
    #以后改进
    
    web_page = 0    #从第一页开始
    space = 30      #百度图片页之间的差值
    while len(addresslist)<num:     #按网址数量 判定是否退出
        prefixion='''http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=r&'''#百度图片
        aim_url = prefixion + "word=" + word + "&pn=" + str(web_page)       #最终网址
        try:
            filt = r'["objURL":|src=]"(http:+?[^\s]+?.[jpg|png|gif])"'      #正则
            filt = re.compile(filt)
            headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ''Chrome/51.0.2704.63 Safari/537.36'} #头部
            req = urllib.request.Request(url=aim_url,headers=headers)
            open_url = urllib.request.urlopen(req).read().decode()
            #decode() 转码 缺省值为str    也可以用str转
            # read()将http response文件转化问byte文件
            # print(text.decode("utf-8")) # 转化以后才可以print
            #text.decode("utf-8")
        except:
            messagebox.showerror("错误","打开网址错误")
            return
        filt = re.compile(filt)
        ll = re.findall(filt,open_url)  #匹配
        j = 0
        for i in ll:
            if i not in addresslist and len(addresslist)<num:  #不含且<num添加
                addresslist.append(i)
            j+=1
        web_page = web_page + space
    return addresslist

def getpicture(road,url,num):
    global panding
    if panding ==1:  #判定开始否
        messagebox.showwarning("警告","已经在开始了")
        return
    if(road==roadFRAME or url==urlFRAME):
        messagebox.showwarning('警告','输入错误')
        return False
    panding = 1
    L = get_baiduimage(url, num)
    #pprint.pprint(L)
    #print("\n",len(L))
    road=road+'/'
    Num = 0
    for tmp in L:
        Num+=1
        f=open(road+str(Num) + '.' + tmp.split('.')[-1],'wb')
        try:
            f.write((urllib.request.urlopen(tmp)).read())
            l.insert(END,"成功:"+tmp)
        except:
            Num-=1
            l2.insert(END,'失败:'+tmp)
        finally:
            f.close()
    messagebox.showinfo('信息','你获得 %d 张图片'%Num)
    panding = 0
    
def onFlip():
    label.config(bg=random.choice(color),fg=random.choice(color))  #杀马特闪
    root.after(250,onFlip)

def get_url(f1l2):
    global url
    url = simpledialog.askstring("网址","请输入网址")
    f1l2.config(text=url)
    
def get_directory(f2l2):
    global road
    road = filedialog.askdirectory()
    f2l2.config(text=road)

def get_num(f3l2):
    global num
    num = simpledialog.askinteger("开始数字","请输入开始数字")
    f3l2.config(text=num)

def Startasthread(road,url,num):
    t = threading.Thread(target=(lambda:getpicture(road, url, num)))  #线程多开
    t.start()

root=Tk()
root.title("爬取图片")
root.geometry('800x300')
#geometry:几何结构   改变窗口大小 格式为 ‘宽x高’中间为'x'不可变
root.resizable(width=False,height=False)
#resizable:可改变的   False代表不可变   True代表可变
label=Label(root,text='爬取图片',relief=RAISED)
onFlip()
label.pack(side=TOP,expand=YES,fill=X)
f1 = Frame(root)
url = urlFRAME
Label(f1,text="请输入目标网址:").grid()
f1l2 = Label(f1)
Button(f1,text="输入",command=(lambda f1l2=f1l2:get_url(f1l2)))\
.grid(row=0,column=1)
#Entry(f1,width=50,textvariable=url).grid(row=0,column=1)
f1l2.grid(row=0,column=2)    #如果grid pack place 了就不能修改值了
f1.pack()
#input url
#fill=X 不受expand影响      fill=Y当expand=1时才可以使用 对BOTH也一样 expand默认0
#且fill需要widget设置后才可以使用

#f1 f2之间 用Frame方法就可以实现“换行”操作

f2=Frame(root)
road = roadFRAME
Label(f2,text="请输入文件目录：").grid(row=1)
f2l2 = Label(f2)
Button(f2,text="打开",command=(lambda f2l2=f2l2:get_directory(f2l2))).grid(row=1,column=1)
#Entry(f2,width=50,textvariable=road).grid(row=1,column=1)
f2l2.grid(row=1,column=2)
f2.pack()
#input road     有了grid就不用pack了


f3=Frame()
num = 0
Label(f3,text='爬取图片数量（数字）：').grid(row=2)
f3l2 = Label(f3)
Button(f3,text="输入",command=(lambda f3l2=f3l2:get_num(f3l2)))\
.grid(row=2,column=1)
f3l2.grid(row=2,column=2)
#Entry(f3,width=20,textvariable=num).pack(side=RIGHT)
f3.pack()

f4=Frame(root)
Button(f4,text="开始",command=lambda:(Startasthread(road,url,num))).pack(side=LEFT,fill=BOTH,expand=1)
Button(f4,text="退出",command=Quit).pack(side=RIGHT,fill=BOTH,expand=1)
#tkinter中destroy函数可以退出   在shell下也可以   better than tkinter.quit
#如果command中函数加了括号就会直接运行函数 且该按钮无效
f4.pack()

f5=Frame()
scrollbar=Scrollbar(f5)
scrollbar.pack(side=LEFT,fill=BOTH,expand=1)
l=Listbox(f5,height=6,width=50)
l.configure(yscrollcommand=scrollbar.set)
#自动调整滚动条大小

l.pack(side=LEFT,fill=BOTH,expand=1)
#pack 与 configure 不能写在一起

scrollbar.config(command=l.yview)
#config设置  Button也有 f=Button(root)   f.config(bg='black',fg='white')
#使上下箭头按钮可以使用

scrollbar2=Scrollbar(f5)
scrollbar2.pack(side=RIGHT,fill=BOTH,expand=1)
l2=Listbox(f5,height=6,width=50)
l2.configure(yscrollcommand=scrollbar2.set)
l2.pack(side=RIGHT,fill=BOTH,expand=1)
scrollbar.config(command=l2.yview)

f5.pack(fill=X,expand=1)

root.mainloop()
