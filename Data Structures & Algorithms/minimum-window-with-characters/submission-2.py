from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        # i have to start with a letter in t so i will keep moving l till i find a letter in t
        # probably need to use a set to check if letter in t
        target = defaultdict(int)
        window = defaultdict(int)
        for c in t:
            target[c] += 1

        needed = len(target)
        have = 0
        l, r = 0,0
        bestLen = float('inf')
        bestStr = ""
        while r < len(s):
            window[s[r]] += 1
            if s[r] in target and window[s[r]] == target[s[r]]:    
                have += 1
            
            while have == needed:
                #found one match now lets move left again and reinitialise
                if (r - l + 1) < bestLen:
                    bestLen = r - l + 1
                    bestStr = s[l:r+1]
                # move the left to new start and try again
                window[s[l]] -= 1
                if s[l] in target and window[s[l]] < target[s[l]]:
                    have -= 1
                l += 1
            r += 1
        return bestStr