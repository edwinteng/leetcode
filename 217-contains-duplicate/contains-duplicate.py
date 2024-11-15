class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for n in nums:
            if n not in d:
                d[n]=1
            else:
                d[n]+=1
                if d[n] == 2:
                    return True
        return False