class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if s == "":
            return 0

        chars = [0]*26

        l = 0
        r = l + 1

        chars[ord(s[l]) - ord('A')] += 1

        best = -1

        while r < len(s):
            chars[ord(s[r]) - ord('A')] += 1
            highfreq = max(chars)
            window = r - l + 1
            if window - highfreq <= k:
                best = max(best,window)
            else:
                chars[ord(s[l]) - ord('A')] -= 1
                l += 1
            r += 1
        return best