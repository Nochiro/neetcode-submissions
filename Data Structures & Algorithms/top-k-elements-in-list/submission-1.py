from collections import defaultdict

class Solution:
    def topKFrequent(self, nums, k):

        # Count frequencies
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1

        # Create buckets
        buckets = [[] for _ in range(len(nums) + 1)]

        # Put numbers into buckets
        for num, count in freq.items():
            buckets[count].append(num)

        result = []

        # Traverse buckets from highest frequency
        for i in range(len(buckets) - 1, 0, -1):

            for num in buckets[i]:
                result.append(num)

                if len(result) == k:
                    return result          