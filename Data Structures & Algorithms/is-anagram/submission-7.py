class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=list(s)
        t=list(t)
        if len(s) != len(t):
            return False
        t.sort()
        s.sort()
        return s==t
    
            

