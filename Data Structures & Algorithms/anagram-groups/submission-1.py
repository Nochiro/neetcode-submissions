class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s = {}
        for word in strs:
            freq = [0]*26
            for alpha in word:
                freq[ord(alpha) - ord('a')] +=1
            key = tuple(freq)
            if key not in s:  
                s[key] = [] 
            s[key].append(word)        
        return list(s.values())   
                