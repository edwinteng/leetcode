class Solution(object):
    def equalFrequency(self, word):
        """
        :type word: str
        :rtype: bool
        """
        d_freq = Counter(word)
        
        for key in d_freq.keys():
            d_freq[key]-=1
            s = set([val for val in d_freq.values() if val>0])
            if len(s) ==1:
                return True
            d_freq[key]+=1
        return False