class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        if n==1:
            return min(matrix[0])
        m = len(matrix[0])
        dp = [[0] * (m+1) for i in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if j==1 :
                    dp[i][j]=matrix[i-1][j-1]+min(dp[i-1][j],dp[i-1][j+1])
                elif j==m:
                    dp[i][j]=matrix[i-1][j-1]+min(dp[i-1][j-1],dp[i-1][j])
                else:
                    dp[i][j]=matrix[i-1][j-1]+min(dp[i-1][j-1],dp[i-1][j],dp[i-1][j+1])
        
        ans = min(dp[n][1::])
        return ans
