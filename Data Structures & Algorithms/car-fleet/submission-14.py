class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        fleet=0
        for i in range(len(speed)):
            t=(target-position[i])/speed[i]
            stack.append((position[i],t))
        stack.sort()
        cur=0
        while stack:
            p, t = stack.pop()
            if (t>cur):
                fleet +=1
                cur=t
        return fleet

        