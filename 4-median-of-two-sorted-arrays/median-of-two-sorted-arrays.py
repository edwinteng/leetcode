class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1,nums2=nums2,nums1
        
        left1,right1 = 0, len(nums1)-1
        left2,right2 = 0, len(nums2)-1
        total= len(nums1)+len(nums2)
        while True:
            mid1= (left1+right1)//2
            mid2 = total//2-mid1-2

            mid_left1 = nums1[mid1] if mid1 >=0 else float('-Inf')
            mid_right1 = nums1[mid1+1] if mid1+1 < len(nums1) else float('Inf')
            mid_left2 = nums2[mid2] if mid2 >=0 else float('-Inf')
            mid_right2 = nums2[mid2+1] if mid2+1 < len(nums2) else float('Inf')

            if mid_left1 <=mid_right2 and mid_left2<=mid_right1:
                if total%2:
                    return min(mid_right1,mid_right2)
                else:
                    return (max(mid_left1,mid_left2)+min(mid_right1,mid_right2))/2
            elif mid_left1 > mid_right2:
                right1 = mid1-1
            else:
                left1 = mid1+1

            

