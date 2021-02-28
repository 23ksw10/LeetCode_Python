class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visit = set()
        visit.add((0,0))
        n = len(grid)
        pq = [(grid[0][0],0,0)]
        ans = 0
        while pq:
            top = heapq.heappop(pq)
            e, i, j = top
            ans = max(e,ans)
            print(ans)
            if i == j == n-1: return ans
            for a,b in [[i+1,j],[i,j+1],[i-1,j],[i,j-1]]:
                if a >= 0 and a < n and b >= 0 and b < n:
                    if (a,b) not in visit:
                        heapq.heappush(pq,(grid[a][b],a,b))
                        visit.add((a,b))
        
