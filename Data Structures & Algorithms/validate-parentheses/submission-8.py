from collections import defaultdict
class Solution:
    def isValid(self, s: str) -> bool:
        map = defaultdict(str)
        map[')'] = '('
        map[']'] = '['
        map['}'] = '{'

        stk = []

        for c in s:
            if c not in map:
                stk.append(c)
            else:
                if stk and stk[-1] == map[c]:
                    stk.pop()
                else:
                    return False
        
        return not stk