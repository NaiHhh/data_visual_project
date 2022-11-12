from bs4 import BeautifulSoup  # 解析网页
import re  # 正则表达式，进行文字匹配
import urllib.request, urllib.error
import time

# re正则表达式
findOrder = re.compile(r'<span>(.*?)</span>')  # 榜单次序
findTitle = re.compile(r'<a class="title" href="//.*?" target="_blank">(.*?)</a>')  # 视频标题
findPlay = re.compile(r'<span class="data-box"><img alt="play" src=".*?"/>([\s\S]*)(.*?)</span> <span class="data-box">')  # 视频播放量
findView = re.compile(r'<span class="data-box"><img alt="like" src=".*?"/>([\s\S]*)(.*?)</span></div></div>')  # 视频评价数


def top100():
    # 声明爬取网站
    baseurl = "https://www.bilibili.com/v/popular/rank/all"
    # 爬取网页
    datalist = getData(baseurl)
    print(datalist)
    return datalist


def getData(baseurl):
    datalist = []
    html = askURL(baseurl)

    soup = BeautifulSoup(html, 'html.parser')  # 解释器
    for item in soup.find_all('li', class_="rank-item"):
        data = []
        item = str(item)

        Order = re.findall(findOrder, item)[0]
        data.append(Order)

        Title = re.findall(findTitle, item)[0]
        data.append(Title)

        Play = re.findall(findPlay, item)[0][0]
        Play = Play.replace(" ", "")
        Play = Play.replace("\n", "")
        Play = Play.replace(".", "")
        Play = Play.replace("万", "0000")
        data.append(Play)

        View = re.findall(findView, item)[0][0]
        View = View.replace(" ", "")
        View = View.replace("\n", "")
        data.append(View)

        datalist.append(data)
    return datalist


def askURL(url):
    # 设置请求头
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML, likeGecko) Chrome/80.0.3987.163Safari/537.36"
    }
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html
