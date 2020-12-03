class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        max_time = releaseTimes[0]
        ans = keysPressed[0]
        for i in range(1, len(releaseTimes)):
            if releaseTimes[i] - releaseTimes[i - 1] > max_time:
                ans = keysPressed[i]
            if releaseTimes[i] - releaseTimes[i - 1] == max_time:
                ans = max(ans, keysPressed[i])
            max_time = max(max_time, releaseTimes[i] - releaseTimes[i - 1])

        return ans