class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ans = 0
        ud = [-1,0,1,0]
        lr = [0,1,0,-1]
        
        m = len(matrix)
        n = len(matrix[0])
        @functools.cache
        def dfs(i,j):
            count = 0
            for k in range(4):
                next_i = i+ud[k]
                next_j = j+lr[k]
                if next_i>=0 and next_i<m and next_j>=0 and next_j<n:
                    if matrix[next_i][next_j]>matrix[i][j]:
                        count =max(count,dfs(next_i,next_j))
            return count+1
        for i in range(m):
            for j in range(n):
                ans=max(ans,dfs(i,j))
        return ans
                    
