class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern)!=len(s.split()):
            return False 
        d_map1 = {}
        d_map2 = {}
        for i,word in enumerate(s.split()):
            if pattern[i] in d_map1 and  d_map1[pattern[i]]!=word:
                return False
            if word in d_map2 and d_map2[word]!=pattern[i]:
                return False
            d_map1[pattern[i]]=word
            d_map2[word]=pattern[i]
        return True