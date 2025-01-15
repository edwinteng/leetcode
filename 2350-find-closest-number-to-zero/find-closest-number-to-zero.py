class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        dis = float('Inf')
        ans = float('-Inf')
        for num in nums:
            if abs(num) < dis or (num > ans and abs(num)==dis):
                dis = abs(num)
                ans = num
        return ans