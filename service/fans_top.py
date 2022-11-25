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
