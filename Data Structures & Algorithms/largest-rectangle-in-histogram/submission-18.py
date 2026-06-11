class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        for i in range(len(heights)):
            height=heights[i]
            width=1
            j=i+1
            while j < len(heights) and heights[i] <= heights[j]:
                j +=1
                width +=1
            j=i-1
            while j >= 0 and heights[i] <= heights[j]:
                j -=1
                width +=1
            area=height * width
            stack.append(area)
            
        stack.sort()
        return stack[-1]

            
        