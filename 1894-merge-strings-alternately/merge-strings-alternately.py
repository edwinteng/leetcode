class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        min_len=min(len(word1),len(word2))
        ans = ['']*(len(word1)+len(word2))
        index = 0
        for element in word1[:min_len]:
            ans[index]=element
            index+=2
        index=1
        for element in word2[:min_len]:
            ans[index]=element
            index+=2
        return ''.join(ans)+word1[min_len:] if len(word1)>=len(word2) else ''.join(ans)+word2[min_len:]