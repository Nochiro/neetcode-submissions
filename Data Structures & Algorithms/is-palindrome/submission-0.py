class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = ""
        for char in s:
            if char.isalnum():
                text += char.lower()
        reverse = ""
        for char in text:
            reverse = char + reverse
        if text == reverse:
            return True
        else:
            return False 
               
                