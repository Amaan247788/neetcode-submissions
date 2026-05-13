class Solution:

    def encode(self, strs: List[str]) -> str:
        #TCP can put special character between the strings
        ans = ""
        for s in strs:
            n = len(s)
            ans += str(n)
            ans += '#'
            ans += s
        return ans
    def decode(self, s: str) -> List[str]:
        #separate the strings by the sentinel
        ans = []
        
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j+1
            j = i + length
            ans.append(s[i:j])
            i = j
                
        return ans
            