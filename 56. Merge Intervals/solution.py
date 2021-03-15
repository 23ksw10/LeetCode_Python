class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        start = intervals[0][0]
        end = intervals[0][1]
        for s,e in intervals:
            if s<=end:
                if e>=end:
                    end = e
            else:
                ans.append([start,end])
                start = s
                end = e
        ans.append([start,end])
        return ans
