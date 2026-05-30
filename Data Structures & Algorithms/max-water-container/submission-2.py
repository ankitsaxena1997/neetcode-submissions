class Solution:
    def maxArea(self, heights: List[int]) -> int:

        i = 0
        j= len(heights)-1
        maxArea=0

        while(i<j):

            currArea=(j-i)*min(heights[i],heights[j])

            if heights[j]>heights[i]:
                i=i+1
            else :
                j=j-1

            maxArea= max(maxArea,currArea)


        return maxArea 
        

        