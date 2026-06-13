class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        longest=0
        windowSet=set()
        for r in range(len(s)):
            while s[r] in windowSet:
                windowSet.remove(s[l])
                l += 1
            windowSet.add(s[r])
            window=(r-l)+1
            longest=max(window,longest)
        return longest
        