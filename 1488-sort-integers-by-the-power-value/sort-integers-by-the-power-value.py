class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        power = {}
        def helper(num):
            step = 0
            x = num
            while x !=1:
                if x in power:
                    return step+power[x]
                if x%2==1:
                    x=3*x+1
                else:
                    x=x/2
                step+=1
            power[x]=step
            return step
        return sorted(range(lo,hi+1),key = helper)[k-1]