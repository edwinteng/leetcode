class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s)< k:
            return False
        d = Counter(s)
        count = 0
        
        for val in d.values():
            if val%2:
                count+=1
        return count<=k