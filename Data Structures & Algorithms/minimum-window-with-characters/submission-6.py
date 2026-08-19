from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        freq = dict(Counter(t))
        count = {}
        min_length = float("inf")
        result = ""
        have = 0
        need = len(freq)
        for r in range(len(s)):
            if s[r] not in count:
                count[s[r]] = 1
            else:
                count[s[r]] += 1
            if s[r] in freq and count[s[r]] == freq[s[r]]:
                have +=1
            while have == need:
                window_length = r-l+1
                if window_length < min_length:
                    min_length = window_length
                    result = s[l:r + 1]
                count[s[l]] -=1
                if s[l] in freq and count[s[l]]< freq[s[l]]:
                    have -=1 
                if count[s[l]] == 0:
                    del count[s[l]]
                l +=1
                 
        return result                        
                        


