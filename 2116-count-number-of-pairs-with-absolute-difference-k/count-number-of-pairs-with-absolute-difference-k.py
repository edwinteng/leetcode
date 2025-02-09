class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        d= Counter()
        cnt = 0
        for i in range(len(nums)):
            cnt+= d[nums[i]+k]+d[nums[i]-k]
            d[nums[i]]+=1
        return cnt