class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        ans = 0
        check = [0] * 101
        for n in nums:
            check[n] += 1
        for i in range(101):
            if check[i] == 1:
                ans += i
        return ans
