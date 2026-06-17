class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        n = len(words) 
        adj = { c:set() for w in words for c in w}
        for i in range(n-1):
            a = words[i]
            b = words[i+1]
            minLen = min(len(a),len(b))
            if len(a) > len(b) and a[:minLen] == b[:minLen]:
                return ""
            for j in range(minLen):
                if a[j] != b[j]:
                    adj[a[j]].add(b[j])
                    break
        
        visit = {} # False = vistied, True = visit + current path
        res = []
        def dfs(c):
            if c in visit:
                return visit[c]
            visit[c] = True

            for nei in adj[c]:
                if dfs(nei):
                    return True
                
            visit[c] = False # No longer in current path
            res.append(c)
        
        for c in adj:
            if dfs(c):
                return ""
        res.reverse()
        return "".join(res)