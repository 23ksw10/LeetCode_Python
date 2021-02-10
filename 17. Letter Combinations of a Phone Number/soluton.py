class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        dtoc = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        def help(index,temp):
            if index == len(digits):
                if temp:
                    ans.append(temp)
                return
            for alp in dtoc[digits[index]]:
                help(index+1,temp+alp)
        help(0,'')
        return ans
            
