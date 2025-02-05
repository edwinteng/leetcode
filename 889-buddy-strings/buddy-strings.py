class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        #len should be equal
        # count should be same
        if len(s)!=len(goal):
            return False
        d1 = Counter(s)
        index = []
        for i in range(len(s)):
            if s[i]!=goal[i]:
                index.append(i)
            if len(index)>2:
                return False
        if len(index)==0 and any(val > 1 for val in d1.values()) or (len(index)==2 and s[index[0]]==goal[index[1]] and s[index[1]]==goal[index[0]]):
            return True
        else:
            return False