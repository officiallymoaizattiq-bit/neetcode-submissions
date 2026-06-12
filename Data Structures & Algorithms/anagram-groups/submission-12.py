class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        HashMap = {}
        for s in strs:
            sort=tuple(sorted(s))
            if sort in HashMap:
                HashMap[sort].append(s)
            else:
                HashMap[sort]=s
        return list(HashMap.values())
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        HashMap = {}
        for i in range(len(strs)):
            sortedStr = tuple(sorted(strs[i]))
            if sortedStr in HashMap:
                HashMap[sortedStr].append(strs[i]) 
            else:
                HashMap[sortedStr] = [strs[i]]
                
        return list(HashMap.values())        


            
        