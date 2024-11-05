class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = set(nums)
        ans = 0
        for num in nums:
            if num-1 not in d:
                num_check = num
                while num_check in d:
                    num_check+=1
                print(num_check)
                ans = max(ans, num_check-num)
        return ans