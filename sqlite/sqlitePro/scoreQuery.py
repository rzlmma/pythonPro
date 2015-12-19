# -*- coding:utf-8 -*-
import xlrd,sqlite3,xlwt

#处理excel表格
def rExcel(filename):
    data = []
    book = xlrd.open_workbook('score.xlsx')        #获取一个Book对象
    table = book.sheet_by_index(0)                   #根据索引获取表格
    name = table.name                                #得到表格的名称
    nrows = table.nrows                              #得到表格的行数
    for i in range(1,nrows):
        rowdata = table.row_values(i)               #获取每一行的数据
        data.append(tuple(rowdata))
    return data

#main函数中的获取信息可以用这个函数表示
def queryData(cursor,sql,*args):
    cursor.execute(sql,args)
    data = cursor.fetchall()
    for item in data:
        item = [i.encode('utf-8') if isinstance(i,basestring) else i for i in item]
        print "id:%d   name:%s   grade:%s  chinese:%d  math:%s  sex:%s"%(tuple(item))
    return data

#将数据写入数据库中
def main(tablename):
    con = sqlite3.connect(database='example.db')
    cursor = con.cursor()
    #创建表格
    try:
       cursor.execute("""CREATE TABLE IF NOT EXISTS score
                                         (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                          name TEXT,
                                          grade TEXT,
                                          chinese INTEGER,
                                          math     INTEGER,
                                          sex      TEXT
                                          )""")
    except Exception,e:
        print e

    # params = rExcel(tablename)
    # cursor.executemany('INSERT INTO score(name,grade,chinese,math,sex) VALUES (?,?,?,?,?)',params)
    # con.commit()

    #获取表格中所有的数据
    for item in cursor.execute("SELECT * FROM score ORDER BY ?",('chinese',)):
         item = [i.encode('utf-8') if isinstance(i,basestring) else i for i in item]
         print "id:%d   name:%s   grade:%s  chinese:%d  math:%s  sex:%s"%(tuple(item))

    print "---------------------------------"

    #获取所有女生的信息
    cursor.execute("SELECT * FROM score where sex=? ORDER BY math",(u'女',))
    for item in cursor.fetchall():
        item = [i.encode('utf-8') if isinstance(i,basestring) else i for i in item]
        print "id:%d   name:%s   grade:%s  chinese:%d  math:%s  sex:%s"%(tuple(item))

    print "---------------------------------------------"
    sql = "SELECT * from score WHERE math BETWEEN ? AND ?  ORDER BY math"
    queryData(cursor,sql,90,100)

#将数据库中的数据写入到excel中
def wExcel():
    book = xlwt.Workbook()
    sheet = book.add_sheet('sheet1',cell_overwrite_ok=True)
    print sheet.name
    sheet.write(0,0,u'姓名')
    sheet.write(0,1,'grade')
    book.save('ScoreWrite.xls')     #文件后缀名是xls不是xlsx,xlwt不兼容兼容office2007



if __name__ == "__main__":
    # main('score.xlsx')
    wExcel()