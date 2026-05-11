from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # make a hashmap and update counts on first loop then 
        # on second decrement if all counts are zero its true
        if len(s) != len(t):
            return False

        char_map = defaultdict(int)
        for i in range(len(s)):
            char_map[s[i]] += 1
            char_map[t[i]] -= 1
        
        for char in char_map:
            if char_map[char] != 0:
                return False
        
        return True
