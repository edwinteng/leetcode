class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        mx,ans = values[0],values[0]

        for i in range(1,len(values)):
            temp_mx = mx
            mx = max(mx,values[i]+i)
            ans = max(ans,temp_mx+values[i]-i)
        return ans