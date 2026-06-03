class Solution:
    def isPalindrome(self, s: str) -> bool:
        special_chars=[",",".","!","?","/"," ","'",":",";"]
        s=s.lower()
        for char in s:
            if char in special_chars:
                s=s.replace(char,'')
        return s==s[::-1]
        