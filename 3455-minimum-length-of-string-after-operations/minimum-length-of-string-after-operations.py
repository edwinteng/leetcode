class Solution:
    def minimumLength(self, s: str) -> int:
        d = Counter(s)
        ans = 0
        for val in d.values():
            if val < 3:
                ans+=val
            else:
                if val%2:
                    ans+=1
                else:
                    ans+=2
        return ans
