class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0]*len(temperatures)
        for index,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                num,i = stack[-1]
                stack.pop()
                ans[i] = index-i
            stack.append((t,index))
        return ans