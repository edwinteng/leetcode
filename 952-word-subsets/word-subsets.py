class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        d = defaultdict(int)
        for word in words2:
            w = Counter(word)
            for key,val in w.items():
                d[key]=max(d[key],val)
        print(d)
        ans = []
        for word in words1:
            w = Counter(word)
            flag = True
            for key,val in d.items():
                if key not in w or w[key]<val:
                    flag=False
            if flag:
                ans.append(word)
        return ans
            
