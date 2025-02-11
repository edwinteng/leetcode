class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        for c in s:
            if c == part[-1]:
                if len(part) == 1:
                    continue
                elif len(stack)>=len(part)-1 and ''.join(stack[-len(part)+1:])+c==part:
                    for i in range(len(part)-1):
                        stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)
        return ''.join(stack)