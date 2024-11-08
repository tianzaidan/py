"""
    爬取目标：https://pic.netbian.com/ 彼岸图网
    首页地址：
    https://pic.netbian.com/4kmeinv/
    第N页
    https://pic.netbian.com/4kmeinv/index_N.html
    https://pic.netbian.com/uploads/allimg/231101/012250-16987729706d69.jpg
    作者：小锋老师
    官网：www.python222.com
"""
import os.path

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}


def crawl_html(url):
    """
        解析网页
    :param url: 请求地址
    :return: 解析后的网页源码
    """
    # 请求网页
    response = requests.get(url=url, headers=headers)
    response.encoding = "gbk"
    return response.text


def download_img(src):
    """
        下载图片
    :param src: 图片路径
    :return:
    """
    # 获取图片名称
    filename = os.path.basename(src)
    print(filename)
    # 下载图片
    try:
        with open(f"./img/{filename}", "wb") as file:
            file.write(requests.get("https://pic.netbian.com" + src).content)
    except:
        print(src, "下载异常")


def parse_html(html):
    # 实例化soup
    soup = BeautifulSoup(html, "lxml")
    # 获取所有图片
    img_list = soup.select("ul.clearfix li a img")
    print(img_list)
    for img in img_list:
        print(img["src"])
        download_img(img["src"])


# # 第一页
# url = "https://pic.netbian.com/4kmeinv/"
# parse_html(crawl_html(url))
# # 第二页到第七页
# for i in range(2, 8):
#     parse_html(crawl_html(f"https://pic.netbian.com/4kmeinv/index_{i}.html"))

urls = ["https://pic.netbian.com/4kmeinv/"] + [
    f"https://pic.netbian.com/4kmeinv/index_{i}.html"
    for i in range(2, 8)
]
print(urls)
for url in urls:
    parse_html(crawl_html(url))
