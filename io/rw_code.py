# -*- coding:utf-8 -*-
"""
mode:
  r, w, r+, w+, a, a+
"""
def rw_mode(param):
    print param.center(40, '=')
    with open('bb.txt', param) as f:
        try:
            f.write('hello world\n  happy new year\n  we are happy family')
        except:
            print "error message: read only"
        finally:
            try:
                for line in f:
                    print line
            except:
                print "error message: write only"


def rw_mode2(file, param):
    print "%s: mode=====>%s"%(rw_mode2.__name__, param)
    with open(file, param) as f:
        for line in f:
            print line
        f.write('this is test\n    we are very happy\n')

        # print "after write"                      #当写完文件后再次读文件的时候出现了问题，不知道出现问题的原因
        # content = f.read()
        # print content
    print "after write:"
    with open(file, param) as f2:
        for line in f2:
            print line


if __name__ == '__main__':
    filename = 'bb.txt'
    rw_mode('r')
    # rw_mode2(filename, 'r+')
    # rw_mode('w')

    # rw_mode('a')


