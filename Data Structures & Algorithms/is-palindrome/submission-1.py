class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = ""
        for char in s:
            if char.isalnum():
                text += char.lower()
        reverse = text[::-1]
        if text == reverse:
            return True
        else:
            return False 
               
                