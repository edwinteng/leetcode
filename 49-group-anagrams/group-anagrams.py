class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a dictionary to maintain the anagram
        # go through strs and save each str as sorted str
        # if there is an duplicate add it to the list with the same key
        # else  add to the dictionary
        d= {}
        for string in strs:
            str_sorted = ''.join(sorted(string))
            if str_sorted not in d:
                d[str_sorted] = [string]
            else:
                d[str_sorted].append(string)
        ans = list()
        for  key in d.keys():
            ans.append(d[key])
        return ans