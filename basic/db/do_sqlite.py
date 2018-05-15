#!/user/bin/env python3
# -*- coding: utf-8 -*-

import os
import sqlite3

# 写===================================

# # 连接数据库，如果不存在，自动创建
# conn = sqlite3.connect('test.db')
# # 获取游标
# cursor = conn.cursor()
# # 游标执行sql
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')

# cursor.execute('insert into user (id, name) values ("1", "VlzZ")')

# print(cursor.rowcount)
# # 关闭游标
# cursor.close()
# # 提交事务
# conn.commit()
# # 关闭连接
# conn.close()

# 读 =============================================
# conn = sqlite3.connect('test.db')
# cursor = conn.cursor()

# cursor.execute('select * from user')
# values =  cursor.fetchall()

# print(values)
# cursor.close()
# conn.close()

# 练习 ==============================================
# 请编写函数，在Sqlite中根据分数段查找指定的名字：

# -*- coding: utf-8 -*-


db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

# 初始数据:
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute(
    'create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()


def get_score_in(low, high):
    ' 返回指定分数区间的名字，按分数从低到高排序 '
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        cursor.execute('select name from user where score >= ? and score <= ? order by score', (str(low), str(high)))
        scores = cursor.fetchall()
        name_list = [x[0] for x in scores]
        print(name_list)
        return name_list
    except Exception as e:
        print(e)
        return []
    finally:
        cursor.close()
        conn.close()



# 测试:
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

print('Pass')
