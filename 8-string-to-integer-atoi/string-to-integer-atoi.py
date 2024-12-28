class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """

        sign = 1
        num = 0
        s= s.strip()
        if len(s)==0:
            return 0
        if s[0] =='-':
            sign = -1
        if s[0] in {'+','-'}:
            s=s[1:]
        for c in s:
            if not c.isdigit():
                break
            num = num*10+int(c) 
            if sign*num >=((2**31)-1):
                return 2**31-1
            if sign*num < (-2**31):
                return -(2**31)
            

                
        return num if sign ==1 else -num
        