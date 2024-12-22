class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel = set(['a','e','i','o','u'])
        ans = ['']*len(s)
        left = 0
        right = len(s)-1
        while left <= right:
            while left <= right and s[left].lower() not in vowel:
                ans[left] = s[left]
                left+=1
            while left <= right and s[right].lower() not in vowel:
                ans[right] = s[right]
                right-=1
            if left<=right:
                ans[left]= s[right]
                ans[right] = s[left]
                left+=1
                right-=1
        return ''.join(ans)