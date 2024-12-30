class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        d= Counter(nums)
        ans = []
        for num in nums:
            if d[num]==1 and num+1 not in d and num-1 not in d:
                ans.append(num)
        return ans