"""
字符串全排列
"""
rest = []

def CalcAllPermutation(alist, begin, to):
    if begin == to:
        rest.append(alist[:])      # 这里不能是alist,如果是alist,所有的结果都一样

    else:
        for j in range(begin, to+1):
            alist[j], alist[begin] = alist[begin], alist[j]
            CalcAllPermutation(alist, begin+1, to)
            alist[j], alist[begin] = alist[begin], alist[j]     # 最后在交换过来


def test(alist, begin, to, step):
    print("begin:%s  to:%s   step:%s" % (begin, to, step))
    if begin == to:
        return

    if step == to:
        return

    for i in range(begin, to):
        if step == 1:
            item = alist[i:i+step]
        else:
            item = alist[i:i+step-1]
            print('item: ', item)
            item.append(alist[begin-1])
        rest.append(item)
    test(alist, begin+1, to, step)
    test(alist, begin+1, to, step+1)


def test_1():
    print("test_1 ....")



if __name__ == "__main__":
    # CalcAllPermutation(['a'], 0,0)
    test(['a', 'b', 'c', 'd'], 0, 4, 1)
    print("rest: %s\n       len(rest):%s" % (rest, len(rest)))