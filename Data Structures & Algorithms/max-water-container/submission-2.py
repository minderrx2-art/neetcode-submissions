class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxVol = 0

        i,j = 0, len(heights) - 1

        while i < j:
            d = j-i
            if heights[i] < heights[j]:
                vol = heights[i] * d
                if maxVol < vol:
                    maxVol = vol
                i+=1
            else:
                vol = heights[j] * d
                if maxVol < vol:
                    maxVol = vol
                j-=1
        return maxVol