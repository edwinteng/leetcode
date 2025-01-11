class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = 0
        d={}
        for right in range(len(nums)):

            if right-k>left:
                del d[nums[left]]
                left+=1
            if nums[right] in d:
                return True
            else:
                d[nums[right]]=d.get(nums[right],0)+1
        return False