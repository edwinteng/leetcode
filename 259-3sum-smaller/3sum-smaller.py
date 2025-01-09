class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()

        ans = 0
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            total = nums[i]
            while j<k:
                if nums[j]+nums[k] >= (target-total):
                    k-=1
                else:
                    ans+=(k-j)
                    j+=1


        return ans