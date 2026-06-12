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


            
        