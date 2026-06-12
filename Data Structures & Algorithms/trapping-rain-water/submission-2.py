class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft=[]
        maxRight=[0]*len(height)
        maxR=0
        maxL=0
        area=0
        for i in range(len(height)):
                maxLeft.append(maxL)
                maxL=max(height[i],maxL)
        for i in range(len(height)-1,-1,-1):
                maxRight[i]=maxR
                maxR=max(height[i],maxR)
        for i in range(len(height)):
            cur = min(maxLeft[i],maxRight[i])-height[i]
            if cur>0:
                area += cur
        return area
