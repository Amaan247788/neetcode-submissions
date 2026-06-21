class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        res = [""]
        resLen = [0]
        def helper(r, l):
            while l >=0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > resLen[0]:
                    res[0] = s[l:r+1]
                    resLen[0] = r - l + 1
                l -= 1
                r += 1
        for i in range(len(s)):
            #odd case
            l,r = i,i
            helper(r, l)
            #even case
            l,r = i, i+1
            helper(r,l)
        return "".join(res)
            