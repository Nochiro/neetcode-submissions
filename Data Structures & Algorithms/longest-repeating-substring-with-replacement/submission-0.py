from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        longest = 0
        freq = Counter()
        for right in range(len(s)):
            freq[s[right]] +=1
            window_length = right - left + 1
            highest_freq = max(freq.values())
            replace = window_length - highest_freq
            while replace > k:
                freq[s[left]] -=1
                left +=1
                window_length = right - left + 1
                highest_freq = max(freq.values())
                replace = window_length - highest_freq
            longest = max(longest, window_length)
        return longest        
