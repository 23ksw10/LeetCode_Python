class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        ans = 0
        tmp = word
        while sequence.count(tmp) :
            tmp += word
            ans+=1
        
        
        return ans
