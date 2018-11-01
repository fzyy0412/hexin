import pymysql as pm
import pandas as pd
import numpy as np
#定义一个sql取数函数
def  post_databases(sql):
    #数据库连接信息
    connDict = {
        'host': '127.0.0.1',
        'user': 'root',
        'password': '111111',
        'db': 'third_data',
        'port': 3306,
        'charset': 'utf8mb4',
        'cursorclass': pm.cursors.DictCursor,
        }
    #构建连接
    conn = pm.connect(**connDict)
   #创建一个游标对象
    cur = conn.cursor()
   #执行sql语句
    try:
       # 执行sql语句
        cur.execute(sql)
       # 提交到数据库执行
        conn.commit()
    except:
        conn.rollback()
        cur.close()

import time
for i in range(100000):
    a = np.random.randint(1,10)
    b = np.random.randint(1,10)
    c = np.random.randint(1,10)
    d = np.random.randint(1,10)
    sql = "INSERT into `data` (time,a,b,c,d) VALUES (now(),{},{},{},{})".format(a,b,c,d)
    post_databases(sql)
    time.sleep(5)