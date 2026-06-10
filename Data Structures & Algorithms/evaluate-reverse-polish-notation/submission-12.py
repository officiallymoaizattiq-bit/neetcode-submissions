class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for s in tokens:
            if s == "+":
                val1=stack.pop()
                val2=stack.pop()
                val2 += val1
                stack.append(val2)
            elif s == "-":
                val1=stack.pop()
                val2=stack.pop()
                val2 -= val1
                stack.append(val2)          
            elif s == "*":
                val1=stack.pop()
                val2=stack.pop()
                val2 *= val1
                stack.append(val2)
            elif s == "/":
                val1=stack.pop()
                val2=stack.pop()
                val2 =int(val2/ val1)
                stack.append(val2)
            else:
                stack.append(int(s))
        return int(stack[-1])


            
        