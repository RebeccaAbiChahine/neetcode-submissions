class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []

        for interval in intervals:
            if len(result) == 0:
                result.append(interval)
                continue
            last = result[-1]
            if interval[0] <= last[1]:
                last[1] = max(last[1], interval[1])
            else:
                result.append(interval)
        return result
