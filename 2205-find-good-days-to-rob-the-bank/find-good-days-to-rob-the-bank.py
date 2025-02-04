class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        if len(security) <time*2:
            return []
        ans = []
        increase = [i for i in range(len(security))]
        decrease = [i for i in range(len(security))]
        for i in range(len(security)-2,-1,-1):
            if security[i] <= security[i+1]:
                increase[i] = increase[i+1]
        for i in range(1,len(security)):
            if security[i-1] >= security[i]:
                decrease[i] = decrease[i-1]
        
        for i in range(len(security)):
            if abs(i-decrease[i])>=time and abs(i-increase[i])>=time:
                ans.append(i)
        return ans

