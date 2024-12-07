class SparseVector:
    def __init__(self, nums: List[int]):
        self.d = {}
        for index,num in enumerate(nums):
            if num!=0:
                self.d[index] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        total = 0
        for key in self.d.keys():
            if key in vec.d:
                total+=self.d[key]*vec.d[key]
        return total




# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)