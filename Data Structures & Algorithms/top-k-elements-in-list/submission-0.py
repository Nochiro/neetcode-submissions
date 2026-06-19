from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fdict = defaultdict(int)       
        for num in nums:
            fdict[num] +=1
        result = []
        for _ in range(k):
            max_freq = 0
            max_num = None
            for num in fdict:
                if fdict[num]> max_freq:
                    max_freq = fdict[num]
                    max_num = num
            result.append(max_num)
            del fdict[max_num]
        return result            