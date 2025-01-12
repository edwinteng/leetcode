class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        num_left = 0
        filtered = []
        for i in range(len(s)):
            if s[i] not in '()':
                filtered.append(s[i])
            elif s[i] == '(':
                filtered.append(s[i])
                num_left+=1
            else:
                if num_left:
                    filtered.append(s[i])
                    num_left-=1
        num_right = 0
        reverse_ans = []
        for i in range(len(filtered)-1,-1,-1):
            if filtered[i] not in '()':
                reverse_ans.append(filtered[i])
            elif filtered[i]==')':
                reverse_ans.append(filtered[i])
                num_right+=1
            else:
                if num_right:
                    reverse_ans.append(filtered[i])
                    num_right-=1
        return ''.join(reverse_ans)[::-1]