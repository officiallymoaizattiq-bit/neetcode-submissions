from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        outputList=[]
        freqTable=defaultdict(int)

        for n in nums:
            freqTable[n] += 1
        
        for i in range(k):
            max=0
            maxKey=0
            for key,val in freqTable.items():
                if val > max:
                    max=val
                    maxKey=key
            outputList.append(maxKey)
            freqTable[maxKey]=0
        return outputList