class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        mi,mid = float('Inf'),float('Inf')
        for num in nums:
            if num < mi:
                mi = num 
            if num > mi and num < mid:
                mid= num 
            if num > mid:
                return True
        return False