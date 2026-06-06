class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        NumberMap={}

        for i in range(len(nums)):
            NumberMap[nums[i]]=i
        for i in range(len(nums)):
            NumNeeded=target-nums[i]
            if NumNeeded in NumberMap and i != NumberMap[NumNeeded] :
                return [i,NumberMap[NumNeeded]]


    
        