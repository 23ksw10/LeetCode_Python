class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        d = {}
        l = 0
        r = len(nums)
        for i in range(r):
            if target - nums[i] in d:
                ans.append(d[target - nums[i]])
                ans.append(i)
                break;

            d[nums[i]] = i

        return ans