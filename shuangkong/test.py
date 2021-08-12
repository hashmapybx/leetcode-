# _*_ coding: utf-8 _*_
# @Time : 2021/8/12/0012 9:46 
# @Author : 流柯 
# @Version：V 0.1
# @File : test.py
# @desc :

# import camelot
# tables = camelot.read_pdf(path)
# tables.export('/root/foo.csv', f='csv', compress=True)

import tabula

path = r"D:\respository\git\leetcode-\shuangkong\resource\2020年就业办就业数据.pdf"
df = tabula.read_pdf(path, encoding='gbk', pages='all')
print(df)
for indexs in df.index:
    # 遍历打印企业名称
    print(df.loc[indexs].values[1].strip())




