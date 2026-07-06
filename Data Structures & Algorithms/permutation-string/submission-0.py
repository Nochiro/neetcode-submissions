from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
       left = 0
       freq = Counter()
       s1_freq = Counter(s1)
       for right in range(len(s2)):
            freq[s2[right]] +=1
            window_length = right - left +1
            if window_length > len(s1):
                freq[s2[left]] -= 1
                left += 1
                window_length = right - left +1
            if window_length == len(s1):
                if freq == s1_freq:
                    return True
       return False        



