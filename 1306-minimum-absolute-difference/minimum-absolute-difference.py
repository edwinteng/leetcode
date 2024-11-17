class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = float('Inf')
        for i in range(1,len(arr)):
            cur = arr[i]
            prev = arr[i-1]
            min_diff = min(min_diff,cur-prev)
        #print(min_diff)
        ans = list()
        for i in range(1,len(arr)):
            cur = arr[i]
            prev = arr[i-1]
            if min_diff == cur-prev:
                ans.append([prev,cur])
        return ans
