"""
    豆瓣电影 Top 250 抓取电影信息，存到excel里面
    使用requests爬取网页，使用bs4解析数据，使用pandas将数据写入Excel
    目标网页：https://movie.douban.com/top250
    分页规律 第N页
    https://movie.douban.com/top250?start=25*(N-1)&filter=
    作者：小锋老师
    官网：www.python222.com
"""

import traceback
import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}

url = "https://movie.douban.com/top250?start=0&filter="


def crawl_html(url):
    """
        解析请求，爬取网页
    :param url: 请求地址
    :return: 网页源码
    """
    response = requests.get(url=url, headers=headers)
    return response.text


def parse_html(html):
    """
        解析网页源码
    :param html: 页面源码
    :return: 页面 电影对象信息列表   [ {'':''},{},{}  ]
    """
    # 实例化soup
    soup = BeautifulSoup(html, "lxml")
    # 获取所有电影DOM
    movie_list = soup.select("ol.grid_view li")
    # print(movie_list)
    # 电影数据对象列表
    movie_data_list = []
    for movie in movie_list:
        try:
            rank = movie.select_one("div.pic em").text  # 获取排名
            title = movie.select_one("div.info span.title").text  # 获取电影名称
            info = movie.select_one("div.bd p").text.strip()  # 获取电影描述信息
            rating_num = movie.select_one("div.star span.rating_num").text  # 获取评分
            comment_count = movie.select("div.star span")[3].text.replace("人评价", "")  # 获取评论数
            quete_dom = movie.select_one("p.quote span.inq")
            quote = ""
            if quete_dom:
                quote = quete_dom.text
            # quote = movie.select_one("p.quote span.inq").text  # 获取电影描述
            movie_data_list.append({
                "rank": rank,
                "title": title,
                "info": info,
                "rating_num": rating_num,
                "comment_count": comment_count,
                "quote": quote
            })
        except:
            print(movie.select_one("div.pic em").text, "异常", traceback.print_exc())
            continue
    return movie_data_list


def export_excel(datas):
    """
        导出数据到Excel
    :param datas: 数据
    :return:
    """
    df = pd.DataFrame(datas)
    df.to_excel("豆瓣电影TOP250.xlsx")


datas = []  # 所有电影数据
for i in range(1, 11):  # 遍历10页
    start = 25 * (i - 1)
    url = f"https://movie.douban.com/top250?start={start}&filter="
    print(url)
    movie_data_list = parse_html(crawl_html(url))
    datas += movie_data_list

export_excel(datas)
