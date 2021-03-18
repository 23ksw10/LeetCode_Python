class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for start, end in zip(l,r):
            t = sorted(nums[start:end+1])
            if len(t) < 3:
                ans.append(True)
                continue
            check = True
            for i in range(1,len(t)):
                if t[i]-t[i-1] != t[1] - t[0]:
                    ans.append(False)
                    check = False
                    break
            if check :
                ans.append(True)
    
                    
        return ans
        
