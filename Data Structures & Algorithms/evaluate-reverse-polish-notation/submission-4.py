class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for i in tokens:
            if i not in ["*", "/","+", "-"]:
                stack.append(i)
            
            else:
                print(stack)
                op2 = int(stack.pop())
                op1 = int(stack.pop())

                if i == "+":
                    stack.append(op1 + op2)
                elif i == "-":
                    stack.append(op1 - op2)
                elif i == "*":
                    stack.append(op1 * op2)
                elif i == "/":
                    stack.append(int(op1 / op2))
                    
                
                
        return int(stack[-1])


            