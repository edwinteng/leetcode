class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        min_int, max_int = -2**31, 2**31 - 1
        s = str(x)
        sign = 1
        if s[0]=='-':
            sign = -1 
            s=s[1:]
        s = s[::-1]
        if sign*int(s)> max_int:
            return 0
        if sign*int(s)< min_int:
            return 0
        return int(s) if sign==1 else -int(s)
