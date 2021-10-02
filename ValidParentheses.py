class Solution:
    def ValidParentheses(self, str):
        stack = []
        for bracket in str:
            if bracket == '[' or bracket == '{' or bracket == '(':
                stack.append(bracket)
                # print(stack)
                continue
            elif bracket == ']' or bracket == '}' or bracket == ')':    
                if(stack != [] and bracket == ']' and stack[-1]=='['):
                    stack.pop()
                elif(stack != [] and bracket == '}' and stack[-1]=='{'):
                    stack.pop()             
                elif(stack != [] and bracket == ')' and stack[-1]=='('):
                    stack.pop()
                else:
                    return False
        
        if len(stack) != 0:
            print('false')
        else:
            print('true')

str1 = "()"
Solution().ValidParentheses(str1)