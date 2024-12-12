class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def helper(n):
            if n == 1:
                return [1]
            if n == 2:
                return [1,1]
            row = helper(n-1)
            ans = [1]
            for i in range(1,len(row)):
                ans.append(row[i-1]+row[i])
            ans.append(1)
            return ans
        final_ans = []
        for i in range(1,numRows+1):
            final_ans.append(helper(i))
        return final_ans 
