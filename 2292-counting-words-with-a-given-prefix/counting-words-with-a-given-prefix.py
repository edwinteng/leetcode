class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        d = {}
        for word in words:
            if word.startswith(pref):
                d[pref]=d.get(pref,0)+1
        return 0 if pref not in d else d[pref]