import csv
import json

if __name__ == '__main__':
    with open('番剧排名.csv', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            # print(row)
            print(row[2])

