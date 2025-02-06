class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if arr[0]>k:
            return k
        left, right = 0, len(arr)

        while left < right:
            mid = left+(right-left)//2
            if arr[mid]-mid-1<k:
                left = mid+1
            else:
                right = mid
        #missing for the current
        return arr[left-1]+k-(arr[left-1]-(left-1)-1)