class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in range(len(tokens)):
            
            if tokens[i] == "+":
                stack.append(int(stack.pop())+int(stack.pop()))
            elif tokens[i] == "*":
                stack.append(int(stack.pop())*int(stack.pop()))
            elif tokens[i] == "-":
                stack.append(-int(stack.pop())+int(stack.pop()))
            elif tokens[i] == "/":
                a=int(stack.pop())
                b=int(stack.pop())
                stack.append(int(b/a))
            else:
                stack.append(int(tokens[i]))
            i+=1
            print(stack)
        return stack[0]
            
            