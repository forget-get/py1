# coding=utf-8
# import pymysql  #导入PyMySQL包
# #连接数据库
# con = pymysql.connect(
#     host='127.0.0.1',
#     port=3306,
#     user='wufu',
#     password='qwe123',
#     db='wode',
#     charset='utf8'
# )
# #定义游标
# cursor = con.cursor()
# cursor.execute('select * from college')
# all = cursor.fetchall()

# idcard = '''
# create table idcard(
# id int primary key ,
# name varchar(5),
# age int ,
# sex  varchar(2))
# '''
# cursor.execute(idcard)
# inset = cursor.execute("insert into idcard(id,name,age,sex) values(1,'姚涛',18,'男')")
# cursor.execute('commit')
# update = cursor.execute("update idcard set name='菜鸟' where name='姚涛'")
# cursor.execute('commit')
# cursor.execute("select * from idcard")
# one = cursor.fetchone()
# print(one)
# cursor.execute("delete from idcard where id=1")
# cursor.execute('commit')

# con.commit()    #提交所有
# cursor.close()  #关闭游标
# con.close()     #关闭连接



import redis

re = redis.Redis(host='127.0.0.1',port='6379')
# re.set('num',11)
# print(re.get('num').decode('utf8'))
# re.set('name','菜鸟')
# print(re.get('name').decode('utf8'))
# re.expire('num',20)
# re.mset(age=18,sex='男')
# re.incr('num')
# re.incr('num',10)
# print(re.get('num'))
# re.decr('num',10)
# print(re.get('num'))
# import os
#
# re.hmset('idcard',{'name':'菜鸟','age':18})
# a = re.hgetall('idcard')
# print(a)
# a = b'\xe8\x8f\x9c\xe9\xb8\x9f'
# print(a.decode('utf8'))
#











