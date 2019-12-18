'''
write_db.py    commit/rollback
'''

import pymysql
# jjk123
# 1.连接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user ='root',
                     password='123456',
                     database ='stu',
                     charset='utf8')

# 2.生成游标对象(操作数据库执行sql语句,获取结果的对象)
cur = db.cursor()

# 3. 利用游标对象执行各种SQL语句
# 3.2 执行write操作,---->> commit / rollback
try:
    # 3.1.1 插入insert操作
    sql = "insert into class values(3,'hi',27,'w',60);"
    cur.execute(sql)
    # **************************************
    sql = "insert into class values(9,'lim',18,'m',80);"
    cur.execute(sql)
    # **************************************
    sql = "insert into class values(%s,%s,%s,%s,%s);"
    cur.execute(sql,[12,'ti',15,'m',99])
    db.commit()   # 提交结果,立即刷新"缓冲区",将data写入数据库.

    # 3.1.2 update修改操作
    sql = "update class set score=101 where name='keke';"
    cur.execute(sql)
    db.commit()

    # 3.1.3 delete 删除操作
    sql = "delete from  class  where name='hi';"
    cur.execute(sql)
    db.commit()

     # 3.1.4 update 修改 语句
    list01 = [(21,1),(20,2),(30,6)]
    sql ="update class set score=score-11,age=%s where id=%s;"
    cur.executemany(sql,list01)
    db.commit()

    #  3.1.5 update 修改 语句
    list01 = [10,9,12]
    sql ="update class set age=age+3 where id=%s;"
    cur.executemany(sql,list01)
    db.commit()
except Exception as e:
    print(e)
    db.rollback()   # 回滚 ,没有写入到数据库的操作召回

# 4. 关闭游标/数据库
cur.close()
db.close()

