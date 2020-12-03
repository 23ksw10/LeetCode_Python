class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        m=Counter(s)
        ans=0
        odd=0;
        for k in m.values():
            if k%2 == 0 : ans += k
            else :
                odd=1
                ans+=k-1
        return ans+1 if odd else ans 