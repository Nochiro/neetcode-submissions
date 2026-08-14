class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total > 0:
                    k -= 1
                elif total < 0:
                    j +=1
                else:
                    res.add((nums[i], nums[j], nums[k])) 
                    j +=1
                    k -=1      
        return [list(x) for x in res]            