class Solution:
    def trap(self, height: List[int]) -> int:
        max_water = 0
        for i in range(len(height)):
            left_max = 0
            right_max = 0
            for j in range(i):
                if height[j] > left_max:
                    left_max = height[j]
            for j in range(i+1, len(height)):
                if height[j] > right_max:
                    right_max = height[j] 
            water = min(left_max, right_max) - height[i] 
            if water > 0:
                max_water += water
        return max_water                      