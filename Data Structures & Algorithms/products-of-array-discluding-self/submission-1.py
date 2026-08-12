class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        s = 1
        res = []
        zero_count = 0

        # Calculate product of non-zero numbers
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                s *= num

        # More than one zero
        if zero_count > 1:
            return [0] * len(nums)

        # Exactly one zero
        elif zero_count == 1:
            for num in nums:
                if num == 0:
                    res.append(s)
                else:
                    res.append(0)

        # No zeros
        else:
            for num in nums:
                res.append(int(s / num))

        return res

           