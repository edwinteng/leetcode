class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(nums[i]) for i in range(len(nums))]
        def cmp(s1,s2):
            if s1+s2 > s2+s1:
                return -1
            else:
                return 1
        nums = sorted(nums,key=cmp_to_key(cmp))
        return str(int(''.join(nums)))
