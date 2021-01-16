class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:

        seen = {}
        day = 1
        while N >= day:
            ans = list(cells)
            ans[0] = 0
            for i in range(1, len(cells) - 1):
                if cells[i - 1] == cells[i + 1]:
                    ans[i] = 1
                else:
                    ans[i] = 0
            ans[len(cells) - 1] = 0
            if day > 1 and ans == seen[1]:
                k = day - 1
                if N % k == 0:
                    return seen[k]
                else:
                    return seen[N % k]
            seen[day] = ans
            cells = list(ans)
            day += 1
        return ans