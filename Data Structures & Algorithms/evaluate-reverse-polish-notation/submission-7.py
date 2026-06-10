class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for s in tokens:
            if s == "+":
                val1=int(stack.pop())
                val2=int(stack.pop())
                val2 += val1
                stack.append(val2)
            if s == "-":
                val1=int(stack.pop())
                val2=int(stack.pop())
                val2 -= val1
                stack.append(val2)          
            if s == "*":
                val1=int(stack.pop())
                val2=int(stack.pop())
                val2 *= val1
                stack.append(val2)
            if s == "/":
                val1=int(stack.pop())
                val2=int(stack.pop())
                val2 /= val1
                stack.append(val2)
            if (s != "+" and s != "-" 
            and s != "*" and s != "/") :
                stack.append(s)
        return int(stack[-1])


            
        