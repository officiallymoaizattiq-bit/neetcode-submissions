class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        NumberMap={}

        for i in range(len(nums)):
            NumNeeded=target-nums[i]
            if NumNeeded in NumberMap:
                return [NumberMap[NumNeeded],i]
            NumberMap[nums[i]]=i