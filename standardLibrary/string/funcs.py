# -*- coding:utf-8 -*-
import string
class MyString:
    def test_capwords(self,value):
        """
        capwords(s,seq=None) 与 title()函数功能相似
        """
        for item in map(string.capwords, value):
            print item
        print "======================"
        for item in value:
            if "_" in item:
                item = string.capwords(item, '_')
            else:
                item = string.capwords(item)
            print"item:", item

        print "========title=========="
        for item in value:
            print item.title()

    def test_maketrans(self,fromstr, tostr):
        """
        创建转换表
        """
        letter = string.maketrans(fromstr, tostr)
        s = "we are best friends"
        print"maketrans:", s.translate(letter)


    def test_template(self):
        """
        string.Template
        :return:
        """
        value = {'name': 'Bob', 'age': 23}
        t = string.Template(
            """
            student name: $name
            student age: $age years old
            """
        )
        print "Template:", t.substitute(value)

if __name__ == '__main__':
    value = ['asdf', 'hello world', 'happy_new']
    myObj = MyString()
    myObj.test_capwords(value)
    myObj.test_maketrans('absdc','12345')
    myObj.test_template()