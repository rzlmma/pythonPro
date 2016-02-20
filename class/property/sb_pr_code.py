# -*- coding:utf-8 -*-
"""
在子类中扩展父类的property属性
"""
class People(object):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        print "getting name..."
        return self._name

    @name.setter
    def name(self, value):
        print "setting name to {0}".format(value)
        self._name = value

    @name.deleter
    def name(self):
        print "removing name...."
        del self._name


#扩展多个property
class SubPerson(People):
    @property
    def name(self):
        print "{0} getting name...".format(self.__class__.__name__)
        return super(SubPerson, self).name

    @name.setter
    def name(self, value):
        print "{0} setting name ....".format(self.__class__.__name__)
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print "{0} removing name ...".format(self.__name__)
        super(SubPerson,SubPerson).name.__delete__(self)

#仅在子类中扩展一个方法
class Teacher(People):
    @People.name.getter
    def name(self):
        print"{0} getting name...".format(self.__class__.__name__)
        return super(Teacher,self).name


    #单独扩展setter
    # @People.name.setter
    # def name(self, value):
    #     print "{0} setting name to {1}".format(self.__class__.__name__, value)
    #     super(Teacher, Teacher).name.__set__(self, value)

if __name__ == '__main__':
    s = SubPerson('Lucy')
    print s.name

    s.name = "Ham"
    print s.name
    print"================================="
    t = Teacher('Smath')
    t.name

    t.name = "Joes"
    print t.name
