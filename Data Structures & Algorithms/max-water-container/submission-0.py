class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        maxArea = 0

        while l<r:
            #calc area H X W (H must be smaller of the 2)
            h = min(heights[l], heights[r])
            w = r - l
            area = h*w
            maxArea = max(maxArea, area)
            #move pointer with shorter height
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return maxArea



