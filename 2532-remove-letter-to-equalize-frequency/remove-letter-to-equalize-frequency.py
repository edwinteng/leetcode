class Solution:
    def equalFrequency(self, word: str) -> bool:
        d = Counter(word)
        for char in word:
            d[char]-=1
            s = [val for val in d.values() if val>0]
            if len(set(s))==1:
                return True
            d[char]+=1
        return False