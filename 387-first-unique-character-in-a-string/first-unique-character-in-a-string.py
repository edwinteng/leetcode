class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_set = Counter(s)
        for i,c in enumerate(s):
            if char_set[c] == 1:
                return i
        return -1
