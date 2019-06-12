# -*- coding:utf-8 -*-
class Solution:
    def maxArea(self, height):
        begin = 0
        end = len(height)
        max_area = self.get_max_area(height, begin, end)
        return max_area

    def get_max_area(self, height, begin, end):
        mid = int((begin+end)/2)
        if mid == begin:
            return 0
        else:
            print("begin:%s    end:%s \n" % (begin, end))
            left = self.get_max_area(height, begin, mid)
            right = self.get_max_area(height, mid+1, end)
            mid = self.max_area_accross_mid(height, begin, mid, end)

            print("left:%s   right:%s   mid:%s" % (left, right, mid))
            if left > right and left > mid:
                return left
            elif right > left and right > mid:
                return right
            elif mid > left and mid > right:
                return mid

    def max_area_accross_mid(self, height, begin, mid, end):
        left_area = 0
        r_area = 0
        for i in range(mid-1, begin-1, -1):
            area = (mid-i) * min(height[i], height[mid])
            if area > left_area:
                left_area = area

        for j in range(mid+1, end):
            area = (j-mid-1) * min(height[j], height[mid+1])
            if r_area < area:
                r_area = area

        area = left_area + r_area
        return area


if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]

    s = Solution()
    s.maxArea(height)


