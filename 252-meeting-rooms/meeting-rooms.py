class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        start = sorted([intervals[i][0] for i in range(len(intervals))])
        end = sorted([intervals[i][1] for i in range(len(intervals))])

        start_i,end_i=0,0
        num_overlap,max_overlap =0,0
        while start_i < len(intervals):
            if start[start_i]<end[end_i]:
                
                start_i+=1
                num_overlap+=1
                max_overlap=max(max_overlap,num_overlap)
            else:
                end_i+=1
                num_overlap-=1
        return max_overlap<=1