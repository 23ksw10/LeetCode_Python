class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = [0]*n
        index = [i for i,b in enumerate(boxes) if b == '1']
        for i in range(n):
            ans[i] += sum(abs(i-j) for j in index )
        return ans
