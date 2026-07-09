class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures)
        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                item = stack.pop()
                prev_temp = item[0]
                prev_index = item[1]

                diff = index - prev_index
                output[prev_index] = diff
            stack.append((temp, index))    
        return output    