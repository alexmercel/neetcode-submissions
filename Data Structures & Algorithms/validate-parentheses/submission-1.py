class Solution:
    def isValid(self, s: str) -> bool:
        validp={"(":")", "{":"}","[":"]"}
        stack=[]
        for i in range(len(s)):
            stack.append(s[i])
            print (stack)
            if len(stack)>1:
                if validp.get(stack[-2])==stack[-1]:
                    stack.pop()
                    stack.pop()

            print(stack)
            i+=1

        if not stack:
            return True
        else:
            return False