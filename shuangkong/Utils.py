# _*_ coding: utf-8 _*_
# @Time : 2021/7/20/0020 14:31 
# @Author : 流柯 
# @Version：V 0.1
# @File : Utils.py
# @desc :

import pymysql
import datetime
import time


# 这个代码需要在本地改成定时任务去运行。


def get_conn_sk():
    """
    双控原始互联网的数据库
    :return:
    """

    conn = pymysql.connect(host="61.243.11.118",
                           user="guest",
                           password="gzaqsc@2021",
                           port=3306,
                           database="gzsafety",
                           )
    return conn


def get_conn_zj():
    """
    双控数据采集的中间库
    :return:
    """
    conn = pymysql.connect(host="61.243.10.244",
                           user="yjt_hlw",
                           password="yjthlw123",
                           port=3306,
                           database="database_yjt_hlw",
                           )
    return conn

#

def get_info():
    start = time.time()
    conn = get_conn_sk()
    cursor = conn.cursor()
    # 需要每天去定时统计mysql的数据量
    list_table = []
    list_result = []
    with open("./resource/shuangkong_table_list.txt", 'r') as fin:
        for tab in fin.readlines():
            list_table.append(tab.replace("\n", ''))
    for idx, tab in enumerate(list_table):
        sql = "select count(1) from {}".format(tab)
        cursor.execute(sql)
        list_result.append((tab, cursor.fetchone()[0]))

    cursor.close()
    conn.close()

    # 开始写入中间库
    conn_zj = get_conn_zj()
    cursor_zj = conn_zj.cursor()

    list_zj = []
    for idx, tab in enumerate(list_table):
        sql = "select count(1) from {}".format(tab)
        # print(sql)
        cursor_zj.execute(sql)
        list_zj.append((cursor_zj.fetchone()[0], datetime.datetime.now()))

    list_final = []
    for idx in range(0, len(list_result)):
        list_final.append(list_result[idx] + list_zj[idx])

    print(list_final)
    insert_sql = "insert into statistic_table_data(table_name, source_table_count, des_table_count, update_time) values(%s,%s,%s,%s)"
    insert = cursor_zj.executemany(insert_sql, list_final)
    print('批量插入返回受影响的行数：', insert)
    cursor_zj.close()
    conn_zj.commit()
    print("finished, spend time is {}".format(time.time() - start))






if __name__ == '__main__':
    get_info()
    # print(get_conn_zj())
