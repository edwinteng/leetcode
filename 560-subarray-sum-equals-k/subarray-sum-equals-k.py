class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #get prefix sum
        d={0:1}
        cum_sum = 0
        cnt = 0
        for i in range(len(nums)):
            cum_sum+=nums[i]
            if cum_sum-k in d:
                cnt+=d[cum_sum-k]
            d[cum_sum]=d.get(cum_sum,0)+1
        return cnt
            