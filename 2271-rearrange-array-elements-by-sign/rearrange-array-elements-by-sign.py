class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        gt,sm = [],[]
        for num in nums:
            if num > 0:
                gt.append(num)
            else:
                sm.append(num)
        ans = []
        for i in range(len(gt)):
            ans.append(gt[i])
            ans.append(sm[i])
        return ans