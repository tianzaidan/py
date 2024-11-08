#coding=utf-8
import re
from asyncio import ALL_COMPLETED

import requests
import time
import os
import threading
import concurrent.futures

def get_html(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.RequestException:
        return None

def get_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.content
        else:
            return None
    except requests.RequestException:
        return None

def parse_html(html,reg):
    imgre = re.compile(reg)
    paragraphs = re.findall(imgre,html)
    return paragraphs

def get_pic(k,reg,url,fileroad):
    # return
    #print(k,url,fileroad+" start……")
    text=get_html(url)
    pic_list=parse_html(text,reg)
    if not os.path.isdir(fileroad):
        os.makedirs(fileroad)
    else:
        print(str(k)+fileroad+" existed")
        return
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as execus:
        futures = [execus.submit(get_download,i,fileroad,pic_list) for i in range(len(pic_list))]
    #concurrent.futures.wait(futures,timeout=None,return_when=ALL_COMPLETED)
    print(k ,url+ " "+fileroad+"  end")
    '''
    for i in range(len(pic_list)):
        con=get_content(pic_list[i])
        road=fileroad+"\\"+str(i+1)+"."+pic_list[i].split(".")[-1]
        with open(road,'wb') as file:
            file.write(con)'''
def get_download(i,fileroad,pic_list):
    con=get_content(pic_list[i])
    road=fileroad+"\\"+str(i+1)+"."+pic_list[i].split(".")[-1]
    #print(road)
    with open(road, 'wb') as file:
        file.write(con)
def main():
    #reg = r'''<a target="blank" href="(.*html).*>(.*)</a></h3>'''
    reg = r'''<a target="blank" href="(.*)" id=.*>(.*)</a></h3>'''
    reg_pic=r'''open\('(https.*?)'\);'''
    url_head="https://1727411562-v927.c91z0667.cc/pw/"
    n=51
    m=100
    for i in range(n,m+1):
        url = 'https://1727411562-v927.c91z0667.cc/pw/thread.php?fid=21&page='
        url = url + str(i)
        file_road='''F:\\pic\\丝袜美腿\\'''
        file_road=file_road+str(i)+"\\"
        print(url,file_road)
        # continue
        html = get_html(url)
        print(len(html))
        url_name_list=[]
        if html:
            parsed_info = parse_html(html,reg)
            for j in range(len(parsed_info)):#获取当前页面所有下层页面
                url_name_list.append((url_head+parsed_info[j][0],file_road+parsed_info[j][1]))
        else:
            print('Failed to retrieve HTML content')
            return
        '''
        print(parsed_info[70])
        return'''
        print(len(url_name_list))
        k=0
        '''
        get_pic(k,reg_pic,url_name_list[k][0],url_name_list[k][1])
        return'''
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            futures = [executor.submit(get_pic,k,reg_pic, url_name_list[k][0], url_name_list[k][1]) for k in range(len(url_name_list))]
        '''
        concurrent.futures
        
        k=0
        while k<len(url_name_list):
            threads = []  # 线程列表
            temp=k
            for l in range(1,6):
                if(k>=len(url_name_list)):
                    break
                # print(k,l)
                t=threading.Thread(target=get_pic,args=(k,reg_pic, url_name_list[k][0], url_name_list[k][1]))
                t.start()
                threads.append(t)
                k=temp+l
            for t in threads:
                t.join()
            '''


if __name__ == '__main__':
    main()