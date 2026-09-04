class Solution:
    def trap(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1
        max_left = 0
        max_right = 0

        total_water = 0

        while left < right:

            if height[left] < height[right]:
                max_left = max(max_left, height[left])
                water_trapped = max_left - height[left]
                total_water += water_trapped
                left += 1

            else:
                max_right = max(max_right, height[right])
                water_trapped = max_right - height[right]
                total_water += water_trapped
                right-=1


        return total_water 
        