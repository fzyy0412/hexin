import pymysql as pm
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import time
from sklearn.externals import joblib
from model_api.score_calculate import score_transform_series
#定义一个sql取数函数
def  get_databases(sql):
    #数据库连接信息
    connDict = {
        'host': '172.20.20.197',
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
    cur.execute(sql)
   #获取提取的数据
    result = cur.fetchall()
   #关闭数据库连接
    cur.close()
    return result
def score_transform_series(series, base=600, odds_score=30, times=2):
    '''

    :param x:
    :param base:
    :param odds_score:
    :param times:
    :return:
    '''
    p1 = np.array(series)
    p0 = 1-p1

    odds = p0 / p1
    factor = odds_score / np.log(times)
    offset = base - factor * np.log(1)
    score = np.log(odds) * factor + offset
    score = list(map(lambda s: round(s, 0), score))
    #score = list(map(lambda s: int(s), score))
    return score

max_time = '2018-10-30 14:25:05'

while True:
    connDict = {
        'host': '172.20.20.197',
        'user': 'root',
        'password': '111111',
        'db': 'third_data',
        'port': 3306,
        'charset': 'utf8mb4',
        'cursorclass': pm.cursors.DictCursor,
    }
    # 构建连接
    conn = pm.connect(**connDict)
    # 创建一个游标对象
    cur = conn.cursor()


    sql = "select * from data where time > '{}'".format(max_time)

    # 执行sql语句
    cur.execute(sql)
    # 获取提取的数据
    result = cur.fetchall()

    if len(result)>0:
        df = pd.DataFrame(result)
        max_time = df.iloc[-1, 5]
        id = df.loc[:,'id'].values
        df = df.loc[:,['a','b','c','d']]

        clf_path = 'C:/Users/wangyunyi/Desktop/code/model_api/iris_model.model'
        clf = joblib.load(clf_path)
        y_hat = clf.predict_proba(np.array(df)).ravel()
        y_hat = score_transform_series(y_hat)

        df = dict(zip(id,y_hat))
        df = pd.DataFrame(df, index=range(1)).T.reset_index()
        df.columns = ['id','score']

        for row in df.values:
            idx = row[0]
            scorex = row[1]
            sql ="INSERT into `score_summary` (score,id) VALUES ({},{})".format(scorex,idx)
            cur.execute(sql)
            conn.commit()

    cur.close()
    time.sleep(10)