# -*- coding:utf-8 -*-
"""
python 高级编程 decorator
"""
#无参的decorator
def mydecorator(function):
    def _mydecorator(*args, **kwgs):
        res = function(*args, **kwgs)
        return res
    return _mydecorator

#有参数的decorator
def mydecorator(arg1,arg2):
    def _mydecorator(function):
        def _decorator(*args, **kwargs):
            res = function(*args, **kwargs)
            return res
        return _decorator
    return _mydecorator

#检查参数
rpc_info = {}
def xmlrpc(in_=(),out=(type(None,))):
    def _xmlrpc(function):
        func_name = function.func_name
        rpc_info[func_name] = (in_,out)

        def _check_types(elements,types):
            if len(elements) != len(types):
                print "elemetns:",len(elements)
                print "types:",len(types)
                raise TypeError('arguments count is wrong')
            typed = enumerate(zip(elements,types))
            for index,couple in typed:
                arg,of_right_type = couple
                if isinstance(arg,of_right_type):
                    continue
                raise TypeError('arg #%d should be %s'%(index, of_right_type))

        def __xmlrpc(*args):
            checkable_args= args
            print "check input args:"
            _check_types(checkable_args,in_)
            res = function(*args)
            print "res:",res
            if not type(res) in (list,tuple):
                checkable_res = (res,)
            else:
                checkable_res = res
            print "checkable_res:",checkable_res
            print "check output args:"
            _check_types(checkable_res,out)
            print "argument check is ending!!!"
            return res
        return __xmlrpc
    return _xmlrpc

def testFunc(*args):
    return args

class A(object):
    pass


if __name__ == "__main__":
    aa = A()
    xrpc = xmlrpc((int,str,bool,A),(int,str,bool,A))
    func = xrpc(testFunc)
    xfun = func(23,'asdf',True,aa)
