class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        mapping = {"(":")" , "[":"]" , "{":"}"}
        for i in s:
            if i in mapping:
                stack.append(mapping[i])
            if stack and i == stack[-1]:
                stack.pop()
            elif i in ["}","]",")"]:
                return False
        print(stack)
        if len(stack)>0:
            return False
        return True