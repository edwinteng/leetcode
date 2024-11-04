class Solution:
    def isValid(self, s: str) -> bool:
        # ans,  boolean: True or False
        # bracket mapping, dictionary
        # ) -> (,  } -> {,  ] -> [
        # stack , list
        # index, integer, 0<= index < len(s)
        ans = False
        mapping = {')':'(',"}":"{","]":"["}
        stack = []
        for index in range(len(s)):
            if len(stack)> 0 and s[index] in ')}]' and mapping[s[index]] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[index])
        return True if len(stack) == 0 else False