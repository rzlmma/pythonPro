# -*- coding:utf-8 -*-
"""
heaps are arrays which a[k] <= a[2*k+1] and a[2*k+2]
"""
import heapq


def init():
    heap = []
    for item in [89,34,12,5,19,21]:
        heapq.heappush(heap, item)
    print "heap:",heap
    return heap


def method(heap):
    heapq.heappop(heap)
    print "heap pop:",heap

    heapq.heapreplace(heap,99)
    print "heapreplace:",heap

    print "nlargest:",heapq.nlargest(3,heap)
    print "nsmallest:", heapq.nsmallest(3,heap)


def change_list_heap(plist):
    print "list:",plist
    heapq.heapify(plist)
    print "plist:",plist


if __name__ == '__main__':
    h = init()
    method(h)
    change_list_heap([89,34,12,5,19,21])