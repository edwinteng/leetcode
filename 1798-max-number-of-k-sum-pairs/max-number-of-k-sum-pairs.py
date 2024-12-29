class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = {}
        for num in nums:
            d[num] = d.get(num,0)+1

        num_pair = 0
        for num in nums:
            if k-num in d:
                if k ==num*2 and d[num]>=2:
                    num_pair+=1
                    d[num]-=2
                if k!=num*2 and d[num]>0 and d[k-num]>0: 
                    d[k-num]-=1
                    d[num]-=1
                    num_pair+=1
            
        return num_pair