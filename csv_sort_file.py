import csv
import shutil
import os
import string
import sys

path='./'
report_csv='./resultN.csv'
# result.csv

labels =[]
s=[]
picpath=[]
with open(report_csv, newline='', encoding="utf-8") as csvfile:
    rows = csv.DictReader(csvfile)

    for row in rows:
        string1=(str(row).split(',')[1])
        string2=string1.split("'")[1]
        s.append(string2)

print(s[0])
print(s[0].split(' ')[-1])
# print(row)
# print("s0  ",s[0])
# print("s1  ",s[1])
for i in range(len(s)):
    label=str(s[i][8:13])

    label_int=''.join(filter(str.isdigit, label))
    labels.append(label_int)
    picpath.append(s[i].split(' ')[-1])


# print(labels[0])
# print(picpath[0])
# print(labels[1])
# print(picpath[1])

# 建立資料夾
dirpath = './sort1311N/'
if not os.path.isdir(dirpath):
    os.mkdir(dirpath)

for i in range(1312):
    dirName=dirpath+str(i)+'/'
    if not os.path.isdir(dirName):
        os.mkdir(dirName)

#移動圖片
for i in range(len(labels)):
    if os.path.isfile(picpath[i]):
        picname=(picpath[i].split('\\')[-1])
        print(picname)
        NewPath=dirpath+labels[i]+'/'+picname
        shutil.copyfile(picpath[i],NewPath)

    else:
        print(picpath[i], "檔案不存在。")
        # print("檔案不存在。")





