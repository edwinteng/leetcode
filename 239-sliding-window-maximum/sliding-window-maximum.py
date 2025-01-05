class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        #if len(nums)<=k:
        #    return [max(nums)]
        left = 0
        ans = []
        q = deque()
        for right in range(len(nums)):
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right)


            if left > q[0]:
                q.popleft()
            if right>=k-1:
                left+=1
                ans.append(nums[q[0]])
        return ans