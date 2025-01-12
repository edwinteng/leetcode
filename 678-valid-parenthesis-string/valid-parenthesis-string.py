class Solution:
    def checkValidString(self, s: str) -> bool:

        num = 0
        for i in range(len(s)):
            if s[i] == '(' or s[i]=='*':
                num+=1
            elif num:
                num-=1
            else:
                return False
        num =0
        for i in range(len(s)-1,-1,-1):
            if s[i]==')' or s[i]=='*':
                num+=1
            elif num:
                num-=1
            else:
                return False
        return True
