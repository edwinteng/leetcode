class Solution:
    def maxScore(self, s: str) -> int:
        #s="01001"
        zeros=[0]*(len(s))
        zeros[0]=1 if s[0]=='0' else 0
        for i in range(1,len(s)):
            if s[i]=='0':
                zeros[i]=zeros[i-1]+1
            else:
                zeros[i]=zeros[i-1]
        score = float('-Inf')
        print(zeros)
        cur_score =0
        for i in range(len(s)-2,-1,-1):
            if s[i+1]=='1':
                cur_score+=1
            score = max(score,cur_score+zeros[i])
        
        return score