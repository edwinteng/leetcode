class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m = len(str1)
        n = len(str2)
        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(1,m+1):
            for j in range(1,n+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1],dp[i-1][j])
        i = m
        j = n
        res = []
        while i>0 or j>0:
            if i == 0:
                j-=1
                res.append(str2[j])
            elif j == 0:
                i-=1
                res.append(str1[i])
            else:

                if dp[i][j]==dp[i-1][j]:
                    i-=1
                    res.append(str1[i])
                elif dp[i][j] ==dp[i][j-1]:
                    j-=1
                    res.append(str2[j])
                else:
                    i-=1
                    j-=1
                    res.append(str1[i])
        return ''.join(res)[::-1]
                