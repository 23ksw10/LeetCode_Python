class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) == 1:
            return False
        n = len(deck)
        can = []
        for i in range(2,n):
            print(i)
            if n%i == 0:
                can.append(i)
        from collections import Counter
        d = Counter(deck)
        for c in can:
            ans = True
            for a,b in d.items():
                if b%c != 0:
                    ans = False
                    break
            if ans:
                return True
        return False
