# -*- coding:utf-8 -*-
""" 数据库操作 sqlite3 """
import sqlite3,datetime,traceback

con = sqlite3.connect(database='example.db')
cursor = con.cursor()

#创建表
sql = "CREATE TABLE IF NOT EXISTS student(name VARCHAR(20),sex int(4),major VARCHAR(20)) "
cursor.execute(sql)

cursor.execute("""CREATE TABLE IF NOT EXISTS
                  score(id INTEGER PRIMARY KEY AUTOINCREMENT ,
                  name VARCHAR(20),
                  grade INTEGER ,
                  testDate DATETIME)""")



#插入一行数据
sqlInsert = "insert into student values('%s','%d','%s')"%('Lucy',0,'computer')
try:
    cursor.execute(sqlInsert)
except:
    traceback.print_exc()

cursor.execute('INSERT INTO score(name,grade,testDate) VALUES(?,?,?)',('Sam','99',datetime.datetime.now()))

#插入多行数据
params = [('Sam',0,'english'),('Spam',1,'math'),('Joe',0,'chinese')]
cursor.executemany('INSERT INTO student VALUES (?,?,?)',params)

#更新数据
cursor.execute('UPDATE student SET sex=? WHERE name=?',(1,'Joo'))
con.commit()                       #保存插入的数据

#修改表结构
#添加一列
cursor.execute('ALTER TABLE student ADD COLUMN age int(10) ')


#删除一列数据
cursor.execute('DELETE FROM student WHERE name=?',('张三',))


#获取数据
for item in cursor.execute('select * from student where sex = ?',(0,)):
    print "name:%s   sex:%s   major:%s  age:%s"%(item)


#fetchall获取数据
cursor.execute('SELECT * FROM student WHERE major=? AND sex=?',('chinese',1))
data = cursor.fetchall()
for item in data:
    print "name:%s   sex:%s   major:%s  age:%s"%(item)

con.close()
