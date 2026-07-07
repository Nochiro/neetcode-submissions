from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        need = Counter(t)
        freq = Counter()
        formed = 0
        required = len(need)

        best_length = float('inf')
        best_left = 0
        best_right = 0

        for right in range(len(s)):
            ch = s[right]
            freq[ch] += 1

            # Check if current window is valid`
            
            if freq[ch] == need[ch]:
                formed +=1
                    

            while formed == required:
                # Update answer
                current_length = right - left + 1
                if current_length < best_length:
                    best_length = current_length
                    best_left = left
                    best_right = right

                # Shrink the window
                left_char = s[left]
                freq[left_char] -= 1
                
                if freq[left_char] < need[left_char]:
                    formed -= 1
                left += 1

                # Recompute validity
        if best_length == float('inf'):
            return ""

        return s[best_left:best_right + 1]  
                    

