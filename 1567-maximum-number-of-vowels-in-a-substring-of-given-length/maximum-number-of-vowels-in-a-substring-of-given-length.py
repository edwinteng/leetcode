class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        d =set(['a','e','i','o','u'])
        cur_vow = 0
        for i in range(k):
            if s[i] in d:
                cur_vow+=1
        max_vow = cur_vow
        for i in range(k,len(s)):
            if s[i] in d:
                cur_vow+=1
            if s[i-k] in d:
                cur_vow-=1
            max_vow =max(max_vow,cur_vow)
        return max_vow