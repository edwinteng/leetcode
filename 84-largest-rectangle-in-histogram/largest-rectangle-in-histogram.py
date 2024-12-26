
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack=[]
        max_area = 0
        for index,height in enumerate(heights):
            start_index = index
            while stack and stack[-1][0] > height:
                val,i = stack.pop()
                max_area = max(max_area,val*(index-i))
                start_index = i
            stack.append((height,start_index))
            #max_area = max(max_area,height)
        for val,i in stack:
            max_area=max(max_area,val*(len(heights)-i))

        return max_area
        