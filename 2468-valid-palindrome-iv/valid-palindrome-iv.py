class Solution:
    def makePalindrome(self, s: str) -> bool:
        
        start,end = 0,len(s)-1
        cnt = 0
        while start < end:
            if s[start]!=s[end]:
                cnt+=1
            start+=1
            end-=1

        return cnt<=2