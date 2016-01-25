# -*- coding:utf-8 -*-
"""
https://docs.python.org/2/library/array.html
array
array(typecode, initializer) like list
"""
from array import array
def init():
    array_c = array('c', 'happy')
    print "array_c:"
    print "array_c:%s   itemsize:%d   buffer_info:%s"%(array_c, array_c.itemsize, array_c.buffer_info())

    array_i = array('i', [3,4,5])
    print "array_i:"
    print "array_i:%s   itemsize:%d   buffer_info:%s"%(array_i, array_i.itemsize, array_i.buffer_info())
    return array_c, array_i


def change_array_c(array_c, array_i):
    # append
    for item in ['w', 89]:
        if isinstance(item, str):
            array_c.append(item)
        else:
            array_i.append(item)

    #extend
    for item in ['year', [23,12,14]]:
        if isinstance(item, str):
            array_c.extend(item)
        else:
            array_i.extend(item)

    #fromstring fromlist
    for item in ['world',[1,2,3]]:
        if isinstance(item, str):
            array_c.fromstring(item)
        else:
            array_i.fromlist(item)
    print "add to array_c:",array_c
    print "add to array_i:",array_i

    # remove
    array_c.remove('h')
    print "remove h from array:",array_c
    array_c.pop()
    print "pop the last item from array:", array_c

    #count
    counter = array_c.count('h')
    print "the count of h:",counter
    return array_c, array_i

def do_files(array_c):
    with open('file.txt', 'w+') as f:
        array_c.tofile(f)


if __name__ == '__main__':
    ac, ai = init()
    change_array_c(ac, ai)
    do_files(ac)
