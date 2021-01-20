class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        length = [min(l) for l in rectangles]
        from collections import Counter
        answer = Counter(length)
        max_len = max(answer.keys())
        return answer[max_len]
