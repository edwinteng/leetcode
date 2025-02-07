class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        d = Counter()
        for i in range(lowLimit,highLimit+1):
            box=0
            for c in str(i):
                box+=int(c)
            d[box]+=1
        return max(d.values())