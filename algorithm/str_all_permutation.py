"""
字符串全排列
"""
rest = []

def CalcAllPermutation(alist, begin, to):
    if to == 1:
        return

    if begin == to:
        rest.append(alist[0:to+1])

    else:
        for j in range(begin, to+1):
            alist[j], alist[begin] = alist[begin], alist[j]
            CalcAllPermutation(alist, begin+1, to)
            alist[j], alist[begin] = alist[begin], alist[j]




if __name__ == "__main__":
    CalcAllPermutation(['a','b','c', 'd'], 0,3)
    print("rest: %s\n       len(rest):%s" % (rest, len(rest)))