class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output=[]
        l=0
        r=k
        while r<=len(nums):
            maximum=nums[l]
            for i in range (k):
                maximum=max(maximum,nums[l+i])
            output.append(maximum)
            r +=1
            l +=1
        return output
        