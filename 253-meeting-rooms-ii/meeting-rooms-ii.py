class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = sorted([intervals[i][0] for i in range(len(intervals))])
        end = sorted([intervals[i][1] for i in range(len(intervals))])
        start_i,end_i = 0,0
        count,max_count=0,0
        while start_i < len(intervals):
            if start[start_i]<end[end_i]:
                count+=1
                start_i+=1
                max_count=max(max_count,count) 
            else:
                count-=1
                end_i+=1
        return max_count
            