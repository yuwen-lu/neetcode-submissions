class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
            elif len(stack) == 0:
                return False
            else:
                    
                if c == ')':
                    if stack[-1] != '(':
                        return False
                    else:
                        stack.pop()
                if c == ']':
                    if stack[-1] != '[':
                        return False
                    else:
                        stack.pop()
                if c == '}':
                    if stack[-1] != '{':
                        return False
                    else:
                        stack.pop()
            
        if len(stack) == 0:
            return True
        else:
            return False