class Solution:
    def maxArea(self, height):
        
        start = 0
        end = len(height) - 1
        current_area = 0 
        max_area = 0
        while start < end:
            current_area = (end - start) * min(height[start], height[end])
            max_area = max(current_area, max_area)
            # print(start, end, current_area, max_area, height[start], height[end])

            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
            
        return max_area


