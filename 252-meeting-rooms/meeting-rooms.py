class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        intervals.sort()
        for i in range(1,len(intervals)):
            prev_end = intervals[i-1][1]
            cur_start = intervals[i][0]
            if cur_start < prev_end:
                return False
        return True

        