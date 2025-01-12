class Solution:
    def minSwaps(self, s: str) -> int:
        num = 0
        swap = 0
        for i in range(len(s)):
            if s[i] == '[':
                num+=1
            elif num:
                num-=1
            else:
                swap+=1
                num+=1
        return swap
