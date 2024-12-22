class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        d = Counter(arr)
        s = set([val for val in d.values()])
        return len(s)==len(d)