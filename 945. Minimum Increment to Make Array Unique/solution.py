class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        if len(A) < 2:
            return 0
        ans = 0
        need = 0
        A.sort()
        for i in range(1,len(A)):
            if  A[i] > A[i-1]:
                continue
            ans+=(A[i-1]-A[i]+1)
            A[i] = A[i-1]+1
        return ans
