class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = {}
        max_freq = 0
        max_length = 0
        for r in range(len(s)):
            if s[r] not in count:
                count[s[r]] = 1
            else:
                count[s[r]]+=1
            window_length = r - l +1
            max_freq = max(max_freq, count[s[r]])
            replace = window_length - max_freq
            while replace > k:
                count[s[l]] -=1
                l +=1
                window_length = r - l +1
                max_freq = max(max_freq, count[s[r]])
                replace = window_length - max_freq
            max_length = max(max_length, window_length)
        return max_length            
