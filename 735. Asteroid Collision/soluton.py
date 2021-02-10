class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [asteroids[0]]
        for i in range(1,len(asteroids)):
            a = asteroids[i]
            while stack and stack[-1]>0 and a<0 :
                d = a + stack[-1]
                if d > 0:
                    a=0
                    break
                elif d < 0:
                    stack.pop()
                elif d == 0:
                    a = 0
                    stack.pop()
            if a:
                stack.append(a)
                
        return stack
