class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split(' ')
        ans = []
        for i in range(len(words)):
            new_word = words[i]
            if words[i][0].lower() in 'aeiou':
                new_word=words[i]+'ma'
            else:
                new_word=words[i][1:]+words[i][0]+'ma'
            new_word = new_word + 'a'*(i+1)
            ans.append(new_word)
        return ' '.join(ans)

