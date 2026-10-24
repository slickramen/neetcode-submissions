class Solution:
    def merge(self, intervals):
        res = []
        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] >= start and intervals[i][0] <= end:
                end = max(end, intervals[i][1])
            else:
                res.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]

        res.append([start, end])
        return res

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        pos = 0
        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[0]:
                continue
            else:
                pos = max(pos, i+1)
        
        intervals.insert(pos, newInterval)


        res = self.merge(intervals)

        return res



