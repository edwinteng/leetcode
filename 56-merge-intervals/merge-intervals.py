class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # answer,  list()
        # index,  integer,  0< index < len(intervals)
        answer = list()
        index = 0
        # Steps
        #  sort intervals
        intervals.sort()
        #  loop through intervals with index
        for index in range(len(intervals)):
        #  Compare element with answer 
            if len(answer) > 0 and answer[-1][1] >= intervals[index][0]:
                answer[-1] = [answer[-1][0],max(intervals[index][1],answer[-1][1])]
        #  Check if element has overlap with answer
        #  If yes,  merge  
            else:
                answer.append(intervals[index])
        #  If not, add the element to the end
        #  return  answer
        return answer
        