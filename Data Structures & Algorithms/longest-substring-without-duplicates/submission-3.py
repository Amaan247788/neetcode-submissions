class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        chars = set()

        l = 0
        chars.add(s[l])
        r = l + 1

        maxLen = 1
        while r < len(s):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            maxLen = max(maxLen, r-l+1)
            r += 1
        
        return maxLen
