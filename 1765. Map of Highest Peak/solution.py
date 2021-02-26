class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        dq = deque()
        m = len(isWater)
        n = len(isWater[0])
        ans = [[-1] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if isWater[i][j]:
                    dq.append((i,j))
                    ans[i][j] = 0
        ud = [-1,0,1,0]
        lr = [0,1,0,-1]
        while dq:
            k = len(dq)
            i = 0
            while i < k:
                a = dq.popleft()
                for j in range(4):
                    x = a[0] + ud[j]
                    y = a[1] + lr[j]
                    if x >=0 and x < m and y >=0 and y < n:
                        if ans[x][y] == -1:
                            ans[x][y] = ans[a[0]][a[1]] + 1
                            dq.append((x,y))
                i += 1
        return ans
