from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        need = Counter(t)
        freq = Counter()

        best_length = float('inf')
        best_left = 0
        best_right = 0

        for right in range(len(s)):
            freq[s[right]] += 1

            # Check if current window is valid
            valid = True
            for ch in need:
                if freq[ch] < need[ch]:
                    valid = False
                    break

            while valid:
                # Update answer
                current_length = right - left + 1
                if current_length < best_length:
                    best_length = current_length
                    best_left = left
                    best_right = right

                # Shrink the window
                freq[s[left]] -= 1
                left += 1

                # Recompute validity
                valid = True
                for ch in need:
                    if freq[ch] < need[ch]:
                        valid = False
                        break

        if best_length == float('inf'):
            return ""

        return s[best_left:best_right + 1]            

