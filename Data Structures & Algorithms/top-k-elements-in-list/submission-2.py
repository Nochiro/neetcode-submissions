class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num] +=1
            else:
                count[num] = 1 
        sorted_count = sorted(count.items(), key = lambda item : item[1], reverse = True)
        result = []
        for item in sorted_count[:k]:
            result.append(item[0])           
        return result    