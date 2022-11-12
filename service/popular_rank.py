import requests
import parsel
import csv

f = open('B站排行榜数据.csv', mode='a', encoding='utf-8-sig', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['标题', '播放量'])
csv_writer.writeheader()
url = 'https://www.bilibili.com/v/popular/rank/all?spm_id_from=333.851.b_7072696d61727950616765546162.3'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
}
response = requests.get(url=url, headers=headers)
selector = parsel.Selector(response.text)
lis = selector.css('.rank-list li')
dit = {}
dits = []
for li in lis:
    title = li.css('.info a::text').get()    # 标题
    bf_info = li.css('div.content > div.info > div.detail > div.detail-state > span.data-box::text').get().strip()    # 播放量
    dit = {
        '标题': title,
        '播放量': float(str.strip(bf_info, "万"))*1000
    }
    dits.append(dit)
    csv_writer.writerow(dit)
    print(dit)
