class Solution:
    def orArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)-1):
            ans.append(nums[i]|nums[i+1])
        return ans