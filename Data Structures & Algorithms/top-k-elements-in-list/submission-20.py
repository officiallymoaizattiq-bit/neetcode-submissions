from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap=defaultdict(int)
        for n in nums:
            hashmap[n] +=1
        maxHeap=[]
        for n,f in hashmap.items():
            heapq.heappush(maxHeap,(-f,n))
        output=[]
        for i in range(k):
            output.append(heapq.heappop(maxHeap)[1])
        return output
        
        

