class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        current=0
        streak=1
        longest=0
        myset=set(nums)
        for n in myset:
            if n-1 not in  myset:
                current=n
                while current+1 in myset:
                    current += 1
                    streak +=1
                if streak>longest:
                    longest=streak
                streak=1
        return longest
                

            
            
