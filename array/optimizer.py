# _*_ coding: utf-8 _*_
# @Time : 2021/6/26/0026 23:34 
# @Author : 流柯 
# @Version：V 0.1
# @File : optimizer.py
# @desc :

import redis
import pymysql
# 建立连接池

def get_conn():
    """
    获取redis数据库的连接对象
    :return:
    """
    pool = redis.ConnectionPool(host="localhost", port=6379)
    red = redis.Redis(connection_pool=pool)

    return red

def get_mysql_conn():
    conn = pymysql.connect(
        host="47.116.75.250",
        port=3306,
        user="root",
        password="root123",
        database="logInfo",

    )
    return conn



def test():
    r = get_conn()
    r.set("xingqiliu", "Sat.")
    print(r.get("xingqiliu"))
    conn =get_mysql_conn()
    cursor = conn.cursor()
    # 先是在redis里面记录最大的id值
    sql_max_idx = "select max(id) from  server_memory;"
    cursor.execute(sql_max_idx)
    res = cursor.fetchone()
    r.set("max_id",res[0])
    while True:
        # 查询redis
        last_index = r.get("last_index")
        if int(last_index) == int(r.get("max_id")):
            break
        else:
            # 接下来查询数据库就是要接着上一次的索引进行查询
            sql = "select * from server_memory where id > {} and id < {}".format(int(last_index), int(last_index) * 50 + 50 )
            cursor.execute(sql)
            total_list = []
            for idx, value in enumerate(cursor.fetchall()):
                # print(value[0], value[1], value[6])
                total_list.append((value[0]))
                if idx+1 == 4:
                    r.set("last_index", value[6])
            # 在缓存中保存上一次最后处理数据Id
            print(r.get("last_index")) # 缓存的结果来判断下一次查询从那个地方开始处理数据
            sql2 = "insert into tmp(total_memory, insert_date) values (%s, current_timestamp );"
            cursor.executemany(sql2, total_list)
            conn.commit()
    cursor.close()
    conn.close()
    print("finished insert into table;")




if __name__ == '__main__':
    test()


