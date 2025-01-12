class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s)%2:
            return False
        num = 0
        for i in range(len(s)):
            if s[i]=='(' or locked[i]=='0':
                num+=1
            elif num:
                num-=1
            else:
                return False
        num = 0
        for i in range(len(s)-1,-1,-1):
            if s[i]==')' or locked[i]=='0':
                num+=1
            elif num:
                num-=1
            else:
                return False
        return True