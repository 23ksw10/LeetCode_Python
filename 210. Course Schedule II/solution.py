class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import defaultdict
        start = defaultdict(list)
        visit = set()
        cycle = set()
        ans = []
        
        for a,b in prerequisites:
            start[a].append(b)
        
        def dfs(c):
            if c in cycle:
                return False
            if c in visit:
                return True
            cycle.add(c)
            for a in start[c]:
                if dfs(a) == False:
                    return False
            cycle.remove(c)
            visit.add(c)
            ans.append(c)
            return True
        for c in range(numCourses):
            if not dfs(c):
                return []
            
            
        return ans
