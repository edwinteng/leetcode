class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i in range(1,len(intervals)):
            prev_start,prev_end = intervals[i-1][0],intervals[i-1][1]
            cur_start,cur_end = intervals[i][0],intervals[i][1]
            if cur_start < prev_end:
                return False
        return True