import pymysql as pm
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

sql = "INSERT into `score_summary` (score,id) VALUES ({},{})".format(3,'2')

# 执行sql语句
cur.execute(sql)
conn.commit()