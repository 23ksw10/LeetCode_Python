class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        total_l = sum(nums)
        if total_l == 0: return False
        if total_l % 4 !=0 :
            return False
        l = total_l//4;
        nums.sort(reverse = True)
        sums = [0,0,0,0]
        def dfs(index):
            if index == len(nums):
                return all([sums[i] == l for i in range(4)])
            if nums[index]>l :return False
            for i in range(4):
                if sums[i]+nums[index]<=l :
                    sums[i]+=nums[index]
                    if dfs(index+1):
                        return True
                    sums[i]-=nums[index]
                if sums[i] == 0 :
                    return False
            return False
        return dfs(0)
            
