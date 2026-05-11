from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # make a hashmap and update counts on first loop then 
        # on second decrement if all counts are zero its true
        char_map = defaultdict(int)
        for c in s:
            char_map[c] += 1
        
        for c in t:
            if c not in char_map:
                return False
            char_map[c] -= 1
        
        for char in char_map:
            if char_map[char] != 0:
                return False
        
        return True
