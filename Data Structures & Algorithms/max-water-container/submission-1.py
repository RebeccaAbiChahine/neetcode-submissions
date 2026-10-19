class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #we check the width (right - left) and height(min(left, right)) -> w x h = water, maxwater(maxwater, water)
        left = 0
        right = len(heights) - 1
        res = 0
        while left < right:
            currWidth = right - left
            currHeight = min(heights[left], heights[right])
            currWater = currWidth * currHeight
            res = max(res, currWater)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1  
        return res
