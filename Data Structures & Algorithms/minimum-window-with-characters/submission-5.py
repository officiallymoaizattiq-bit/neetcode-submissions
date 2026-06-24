class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dictt={}
        have=0
        dictcurr={}
        shortest=float("inf")
        for i in range(len(t)):
            dictt[t[i]] = 1 + dictt.get(t[i],0)
        need=len(dictt)
        l=0
        for r in range(len(s)):
            dictcurr[s[r]] = 1+ dictcurr.get(s[r],0)
            if s[r] in dictt and dictcurr[s[r]] == dictt[s[r]]:
                have +=1
            while have == need:
                if (r - l + 1) < shortest:
                    shortest = r - l + 1
                    resL, resR = l, r
                dictcurr[s[l]] -= 1
                if s[l] in dictt and dictcurr[s[l]] < dictt[s[l]]:
                    have -=1
                l += 1
        if shortest != float("inf"):
            return s[resL:resR+1] 
        else :
            return ""           
        



        