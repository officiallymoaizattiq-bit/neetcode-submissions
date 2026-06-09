class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        val=""
        for i in range(len(s)):
            char=s[i:i+1]
            if (char == "(" or char == "[" or char == "{"):
                stack.append(char)
            if (char == ")" or char == "]" or char == "}"):
                if stack:
                    val=stack.pop()
                if (char == ")" and val !="("
                or char == "]" and val != "["
                or char == "}" and val != "{"):
                    return False
        if stack:
            return False
        return True



        