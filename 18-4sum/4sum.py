class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = list()
        for i in range(len(nums)-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,len(nums)-2):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                sum_c_d = target-nums[i]-nums[j]
                k = j+1
                l = len(nums)-1
                while k<l:
                    if nums[k]+nums[l]==sum_c_d:
                        ans.append([nums[i],nums[j],nums[k],nums[l]])
                        k+=1
                        l-=1
                        while k<l and nums[k]==nums[k-1]:
                            k+=1
                        while l>k and nums[l]==nums[l+1]:
                            l-=1
                    elif nums[k]+nums[l]<sum_c_d:
                        k+=1
                    else:
                        l-=1
        return ans

