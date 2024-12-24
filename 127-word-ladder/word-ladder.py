class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #if endWord in wordList:
        #    return 0
        pattern = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                p = word[:i]+'*'+word[i+1:]
                pattern[p].append(word)

        q = deque()
        q.append(beginWord)
        visited = set()
        visited.add(beginWord)
        numStep = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word==endWord:
                    return numStep
                for j in range(len(word)):
                    p = word[:j]+'*'+word[j+1:]
                    for w in pattern[p]:
                        if w not in visited:
                            visited.add(w)
                            q.append(w)
            numStep+=1 
        return 0

            