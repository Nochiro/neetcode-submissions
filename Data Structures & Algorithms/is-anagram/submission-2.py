class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars ={}
        chart = {}
        for alphabet in s:
            if alphabet in chars:
                chars[alphabet] +=1
            else:
                chars[alphabet] = 1    
        for alphabet in t:
            if alphabet in chart:
                chart[alphabet] +=1
            else:
                chart[alphabet] = 1        
        return chars == chart
               
                   