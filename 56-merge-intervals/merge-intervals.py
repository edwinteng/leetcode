class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort intervals
        intervals.sort()
        #assign answer to the 1st interval
        ans = []
        ans.append(intervals[0])
        #loop
        for i in range(1,len(intervals)):
            prev_start,prev_end= ans[-1][0],ans[-1][1]
            cur_start,cur_end = intervals[i][0],intervals[i][1]
            if cur_start <= prev_end:
                ans[-1][1] = max(prev_end,cur_end)
            else:
                ans.append(intervals[i])
        return ans

        