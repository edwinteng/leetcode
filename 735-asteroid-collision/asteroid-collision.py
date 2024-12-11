class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            if len(stack)==0 or stack[-1]*ast>0 or (ast>0 and stack[-1]<0):
                stack.append(ast)
                continue
            
            #exclude -> <- and ast is bigger
            while stack and stack[-1]>0 and ast<0 and abs(stack[-1])<abs(ast):
                stack.pop()
            # -> <- and ast is the same
            if stack and ast <0 and stack[-1]>0 and abs(stack[-1])==abs(ast):
                stack.pop()
            # -> <- and ast is small
            elif stack and ast <0 and stack[-1]>0 and abs(stack[-1])>abs(ast):
                continue
            else:
            # <- <-
                stack.append(ast)

        return stack


                

                    

                