class Solution:
    def isPalindrome(self, s: str) -> bool:
        #clean the string by getting rid of:
        # - spaces, make capital letters small, rid of special chars
        s_clean = ""
        for c in s:
            if not c.isalnum():
                continue
            elif c.isupper():
                s_clean += c.lower()
            else :
                s_clean += c
        
        left = 0
        right = len(s_clean) - 1

        while left < right:
            if s_clean[left] != s_clean[right]:
                return False
            else:
                left += 1
                right -= 1
        return True
