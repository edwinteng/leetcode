class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        mapping = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        if len(s) == 0:
            return 0

        num = mapping[s[0]]
        for i in range(1,len(s)):
            cur = s[i]
            prev = s[i-1]
            num+=mapping[cur]
            if cur in 'VX' and prev == 'I':
                num-=2*mapping[prev]
            if cur in 'LC' and prev == 'X':
                num-=2*mapping[prev]
            if cur in 'DM' and prev =='C':
                num-=2*mapping[prev]
        return num