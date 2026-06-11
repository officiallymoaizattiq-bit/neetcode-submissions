class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        maxArea=0
        for i in range(len(heights)):
            while stack and  heights[stack[-1]] > heights[i]:
                popped=stack.pop()
                if not stack:
                    width=i
                else:
                    width=i-stack[-1]-1
                area=heights[popped]*width
                if area > maxArea:
                    maxArea=area
            stack.append(i)
        n=len(heights)
        while stack:
            popped=stack.pop()
            if not stack:
                width=n
            else:
                width=n-stack[-1]-1
            area=heights[popped]*width
            if area > maxArea:
                maxArea=area
        return maxArea 


            
        