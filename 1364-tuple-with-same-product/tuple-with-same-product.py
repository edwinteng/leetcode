class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product = defaultdict(int)
        for i in range(1, len(nums)):
            for j in range(i):
                p = nums[i]*nums[j]
                product[p]+=1
        return sum(val*(val-1)//2 for val in product.values())*8
