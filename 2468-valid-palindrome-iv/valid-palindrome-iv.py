class Solution:
    def makePalindrome(self, s: str) -> bool:

        start,end = 0,len(s)-1
        cnt = 0
        while start < end:
            if s[start]==s[end]:
                start+=1
                end-=1
            else:
                if cnt<2:
                    cnt+=1
                    start+=1
                    end-=1
                else:
                    return False
        return True