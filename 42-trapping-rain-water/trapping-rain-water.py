class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = [0]*len(height)
        right = [0]*len(height)
        left[0] = height[0]
        for i in range(1,len(height)):
            left[i] = max(height[i],left[i-1])
        right[len(height)-1]=height[len(height)-1]
        for j in range(len(height)-2,-1,-1):
            right[j] = max(height[j],right[j+1])
        ans = 0
        for i in range(1,len(height)-1):
            ans += (min(left[i],right[i])-height[i])
        return ans