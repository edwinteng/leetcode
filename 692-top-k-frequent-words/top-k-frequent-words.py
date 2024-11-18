import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = {}
        for word in words:
            if word not in d:
                d[word]=1
            else:
                d[word]+=1
        h = []
        for word in d.keys():
            heapq.heappush(h,[-d[word],word])
        ans = []
        for i in range(k):
            freq_neg,word = heapq.heappop(h)
            ans.append(word)
        return ans