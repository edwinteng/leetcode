class Solution:
    def minimumLength(self, s: str) -> int:
        d = Counter(s)
        ans = 0
        for val in d.values():
            if val < 3:
                ans+=val
            else:
                tmp = val
                while tmp >2:
                    tmp-=2
                ans+=tmp
        return ans
