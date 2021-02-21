class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict
        _in = defaultdict(list)
        _out = defaultdict(list)
        start = []
        count = 0

        for a,b in prerequisites:
            _in[a].append(b)
            _out[b].append(a)
        for i in range(numCourses):
            if not _in[i]:
                start.append(i)
                count += 1
        while start:
            a = start.pop(0)
            for b in _out[a]:
                _in[b].remove(a)
                if not _in[b]:
                    start.append(b)
                    count += 1
                
        return True if count == numCourses else False
