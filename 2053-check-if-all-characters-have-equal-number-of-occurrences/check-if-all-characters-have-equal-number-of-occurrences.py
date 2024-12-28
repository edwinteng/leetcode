class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = Counter(s)
        unique_freq = set([d[key] for key in d.keys()])

        return len(unique_freq)==1