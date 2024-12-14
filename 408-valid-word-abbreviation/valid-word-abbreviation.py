class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        #loop thhroguh word
        # if chr is numeric save the number
        # else  match character with abbr
        #  when number > 0  loop
        #
        i_word = 0
        i_abbr = 0
        while i_word < len(word):

            if i_abbr < len(abbr) and abbr[i_abbr].isdigit():
                cur_abbr=i_abbr
                while i_abbr<len(abbr) and abbr[i_abbr].isdigit():
                    print(abbr[i_abbr])
                    i_abbr+=1
                num_str = abbr[cur_abbr:i_abbr]
                #print(num_str)
                if num_str[0] == '0':
                    return False
                i_word+=int(num_str)
            else:
                if i_abbr< len(abbr) and word[i_word]==abbr[i_abbr]:
                    i_word+=1
                    i_abbr+=1
                    continue
                else:
                    return False
                
        return True if i_word==len(word) and i_abbr ==len(abbr) else False