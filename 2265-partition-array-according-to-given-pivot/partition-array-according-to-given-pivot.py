class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        sm,eq,gr = [],[],[]
        for num in nums:
            if num < pivot:
                sm.append(num)
            elif num>pivot:
                gr.append(num)
            else:
                eq.append(num)
        return sm+eq+gr