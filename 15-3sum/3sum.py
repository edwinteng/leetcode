class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = list()
        nums.sort()
        for i in range(len(nums)-2):
            if i-1>=0 and nums[i]==nums[i-1]:
                continue
            j = i+1
            k=len(nums)-1
            while j<k:
                if nums[j]+nums[k]== -nums[i]:
                    ans.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while k>j and nums[k]==nums[k+1]:
                        k-=1
                elif nums[j]+nums[k] > -nums[i]:
                    k-=1
                else:
                    j+=1
        return ans