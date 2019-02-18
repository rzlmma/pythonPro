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




if __name__ == "__main__":
    CalcAllPermutation(['a'], 0,0)
    print("rest: %s\n       len(rest):%s" % (rest, len(rest)))