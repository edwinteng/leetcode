class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_index = 0
        t_index = 0
        while t_index < len(t) and s_index <len(s):
            if s[s_index]==t[t_index]:
                s_index+=1
                t_index+=1
            else:
                t_index+=1
        return True if s_index==len(s) else False