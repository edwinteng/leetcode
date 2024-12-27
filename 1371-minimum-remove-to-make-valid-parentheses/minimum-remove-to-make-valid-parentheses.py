class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        count_left=0
        count_right =0
        ans = []
        for c in s:
            if c not in '()':
                ans.append(c)
                continue
            if c =='(':
                count_left+=1
                ans.append(c)
            if c ==')':
                if count_left >0:
                    count_left-=1
                    ans.append(c)
        filtered = []
        for c in ans[::-1]:
            if c == ')':
                count_right+=1
                filtered.append(c)
            elif c== '(':
                if count_right>0:
                    count_right-=1
                    filtered.append(c)
            else:
                filtered.append(c)
        return ''.join(filtered[::-1])

