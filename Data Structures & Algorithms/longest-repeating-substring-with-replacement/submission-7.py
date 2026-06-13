class Solution:
    from collections import defaultdict
    def characterReplacement(self, s: str, k: int) -> int:
        longest=0
        l=0
        freq=defaultdict(int)
        for r in range(len(s)):
            freq[s[r]] +=1
            while (r-l+1) - (max(freq.values())) > k:
                freq[s[l]] -= 1
                l += 1
            longest=max(longest,(r-l+1))
        return longest
        