import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        dic = Counter(s)
        ans = ['']*len(s)
        # initialize heap
        h = []
        # loop through dic and add to heap
        for key,val in dic.items():
            heapq.heappush(h,(-val,key))
        most_freq,key = h[0]
        if -most_freq > (len(s)+1)//2:
            return ""
        #print(dic)
        index = 0
        # loop through string
        #for _ in range(len(s)):
        while h:
        # pull chr one by one from heap
            freq,char = heapq.heappop(h)
            print(char)
        # add to string
            for _ in range(-freq):
                ans[index] = char
                index+=2
                if index >= len(s):
                    index = 1
                
        return ''.join(ans)