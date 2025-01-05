class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d_t = Counter(t)
        d_w = Counter()
        left = 0
        valid = 0
        ans_len = float('Inf')
        ans = [-1,-1]
        for right,c in enumerate(s):
            d_w[c] = 1+d_w.get(c,0)
            if c in d_t and d_w[c]==d_t[c]:
                valid+=1
            # if we ever meet the requirement
            while valid ==len(d_t):  
                #update the length of minimum window
                if right-left+1 < ans_len:
                    ans_len=right-left+1
                    ans = [left,right]
                #shrink
                d_w[s[left]]-=1
                #the only reason to update valid is that the window is no longer valid
                if s[left] in d_t and d_w[s[left]]<d_t[s[left]]:
                    valid-=1
                left+=1
        return s[ans[0]:(ans[1]+1)]

