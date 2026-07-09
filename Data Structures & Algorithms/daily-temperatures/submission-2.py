class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures)
        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                prev_temp, prev_index = stack.pop()
                diff = index - prev_index
                output[prev_index] = diff
            stack.append((temp, index))    
        return output    