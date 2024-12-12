class Solution:
    def frequencySort(self, s: str) -> str:
        d = Counter(s)
        ans = ''
        for key,value in sorted(d.items(),key=lambda item:item[1],reverse=True):
            for i in range(value):
                ans+=key
        return ans
