from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        count = {}
        freq = dict(Counter(s1))
        for r in range(len(s2)):
            if s2[r] not in count:
                count[s2[r]] = 1
            else:
                count[s2[r]] +=1
            while r-l+1> len(s1):
                count[s2[l]] -=1
                if count[s2[l]] == 0:
                    del count[s2[l]]
                l+=1
            if count == freq:
                return True
        return False        
