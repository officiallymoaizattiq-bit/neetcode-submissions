class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap={}
        for i,n in enumerate(nums):
            numNeeded=target-n
            if numNeeded in numMap:
                return [numMap[numNeeded],i]
            numMap[n]=i
    
