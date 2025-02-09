class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d = {0:1}
        cum_sum = 0
        ans = 0
        for i in range(len(nums)):
            cum_sum+=nums[i]
            if cum_sum%k in d:
                ans+=d[cum_sum%k]
            d[cum_sum%k] = d.get(cum_sum%k,0)+1
        return ans