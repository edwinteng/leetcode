class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        d=Counter()
        total_pair = 0
        good_pair = 0
        for i in range(len(nums)):
            total_pair+=i-d[nums[i]-i]
            d[nums[i]-i]+=1
        return total_pair