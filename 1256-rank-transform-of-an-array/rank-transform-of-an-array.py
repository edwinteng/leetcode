from bisect import bisect_right
class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        arr_sort = sorted(set(arr))
        return [bisect_right(arr_sort,n) for n in arr]