class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        ans = [intervals[0]]
        for i in range(1,len(intervals)):
            cur_start,cur_end = intervals[i]
            prev_start,prev_end = ans[-1]
            if cur_start <= prev_end:
                new_start = min(cur_start,prev_start)
                new_end = max(cur_end,prev_end)
                ans.pop()
                ans.append([new_start,new_end])
            else:
                ans.append(intervals[i])
        return ans
