import os
import jieba
import collections
import re
import requests
import numpy as np

comment_file_path = 'B站弹幕.csv'


# 爬取弹幕
def spider_page(cid):
    print('正在解析，开始爬取弹幕中。。。。。')
    url = f'https://comment.bilibili.com/' + cid + '.xml'

    headers = {
        'referer': 'xxxxx',
        'User-Agent': 'xxxxx',
        'cookie': "xxxxx"
    }

    resp = requests.get(url, headers=headers)
    # 调用.encoding属性获取requests模块的编码方式
    # 调用.apparent_encoding属性获取网页编码方式
    # 将网页编码方式赋值给response.encoding
    resp.encoding = resp.apparent_encoding

    print(resp.text)

    if resp.status_code == 200:
        # 获取所有评论内容
        content_list = re.findall('<d p=".*?">(.*?)</d>', resp.text)

    if os.path.exists(comment_file_path):
        os.remove(comment_file_path)
    for item in content_list:
        with open(comment_file_path, 'a', encoding='utf-8') as fin:
            fin.write(item + '\n')
            print(item)
    print('-------------弹幕获取完毕！-------------')
    # 获取处理后的数据
    return data_clear()


# 去除分词结果中的无用词汇
def deal_txt(seg_list_exact):
    result_list = []

    with open('stop_words.txt', encoding='utf-8') as f:

        con = f.readlines()

        stop_words = set()

        for i in con:
            i = i.replace("\n", "")  # 去掉读取每一行数据的\n

            stop_words.add(i)

    for word in seg_list_exact:

        # 设置停用词并去除单个词

        if word not in stop_words and len(word) > 1:
            result_list.append(word)

    return result_list


def data_clear():
    # 读取弹幕文件

    with open('B站弹幕.csv', encoding='utf-8') as f:
        data = f.read()

    # 文本预处理 去除一些无用的字符  只提取出中文出来

    new_data = re.findall('[\u4e00-\u9fa5]+', data, re.S)

    new_data = " ".join(new_data)

    # jieba分词将整句切成分词

    seg_list_exact = jieba.cut(new_data, cut_all=True)

    # 去掉无用词汇

    final_list = deal_txt(seg_list_exact)

    # 筛选后统计

    word_counts = collections.Counter(final_list)

    # 获取前100最高频的词

    word_counts_top100 = word_counts.most_common(100)

    # 可以打印出来看看统计的词频

    print(word_counts_top100)

    return list2json(word_counts_top100)


def list2json(danmu):
    a = np.array(danmu)
    print(a)
    # 定义list
    # 获取相关列转list
    x1list = a[:, 0]
    x2list = a[:, 1]

    i = 0
    s = []
    for obj in x1list:
        dict = {"name": x1list[i], "value": x2list[i]}
        i = i + 1
        s.append(dict)
    return s
