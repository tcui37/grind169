class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        for i in range(len(intervals) - 1):
            before, after = intervals[i], intervals[i + 1]
            if after[0] < before[1] or before[0] == after[0]:
                return False
        return True
