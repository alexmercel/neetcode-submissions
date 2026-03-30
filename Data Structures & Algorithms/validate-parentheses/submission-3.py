class Solution:
    def isValid(self, s: str) -> bool:
        validp={"(":")", "{":"}","[":"]"}
        stack=[]
        for i in range(len(s)):
            
            if stack and validp.get(stack[-1])==s[i]:
                    stack.pop()
            else:
                stack.append(s[i])
            i+=1

        if not stack:
            return True
        else:
            return False