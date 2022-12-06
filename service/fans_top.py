import csv


# 获取每一行
def get_fans_data():
    with open('biliUpFans.csv', 'r', encoding="gbk") as f:
        result = []
        ups = []
        fans = []
        reader = csv.reader(f)
        for row in reader:
            ups.append(row[0])
            fans.append(row[1])
        result.append(ups)
        result.append(fans)
        return result


def get_anime_top():
    with open('番剧排名.csv', encoding='utf-8') as f:
        lists = [[], [], [], []]
        result = []
        reader = csv.reader(f)
        for row in reader:
            lists[0].append(row[0])
            lists[1].append(row[2])
            lists[2].append(row[3])
            lists[3].append(row[4])
        for list in lists:
            result.append(list)
        return result

