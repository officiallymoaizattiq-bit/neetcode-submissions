from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        outputList=[]
        freqTable=defaultdict(int)
        maxHeap=[]

        for n in nums:
            freqTable[n] += 1
        
        for num,freq in freqTable.items():
            heapq.heappush(maxHeap,(-freq,num))

        for i in range(k):
            outputList.append(heapq.heappop(maxHeap)[1])

        return outputList