class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        d ={}
        color_distinct = Counter()
        ans = []
        for node,color in queries:
            
            if node in d:
                color_distinct[d[node]]-=1
                if color_distinct[d[node]]==0:
                    del color_distinct[d[node]]
            color_distinct[color]+=1
            d[node]=color
            ans.append(len(color_distinct))
        return ans
