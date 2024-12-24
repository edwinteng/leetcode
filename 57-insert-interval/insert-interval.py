class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        for i in range(len(intervals)):
            if newInterval[1]< intervals[i][0]:
                ans.append(newInterval)
                return ans + intervals[i:]
            elif newInterval[0]>intervals[i][1]:
                ans.append(intervals[i])
            else:
                new_start = min(newInterval[0],intervals[i][0])
                new_end = max(newInterval[1],intervals[i][1])
                newInterval=[new_start,new_end]
        ans.append(newInterval)
        return ans
