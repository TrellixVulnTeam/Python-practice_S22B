#!/user/bin/env python3
# -*- coding: utf-8 -*-

import mysql.connector

conn = mysql.connector.connect(
    user='root', password='Satan1221', database='test')
cursor = conn.cursor()

# cursor.execute(
#     'create table user (id varchar(20) primary key, name varchar(20))')

# cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'VlzZ'])

# print(cursor.rowcount)

# cursor.close()
# conn.commit()
# conn.close()

cursor.execute('select * from user')
users = cursor.fetchall()
print(users)

cursor.close()
conn.close()

