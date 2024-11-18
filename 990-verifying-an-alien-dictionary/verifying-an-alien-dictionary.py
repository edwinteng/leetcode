class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {c: i for i,c in enumerate(order)}

        for i in range(1,len(words)):
            prev_word,cur_word = words[i-1],words[i]
            for j in range(len(prev_word)):
                #case 1
                #  if characters are different 
                #        check order 
                if j< len(cur_word) and cur_word[j]!=prev_word[j]:
                    if d[prev_word[j]]>d[cur_word[j]]:
                        return False
                    else:
                        break
                # if characters are the same
                #        if reaching the end of current word
                #              return False
                #   
                if j==len(cur_word):
                    return False
     

        return True