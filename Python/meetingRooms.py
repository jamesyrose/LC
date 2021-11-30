class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals: list) -> bool:
        """
        O(n log n) time
        O(n) space
        :param intervals:
        :return:
        """
        intervals.sort(key=lambda x: x.start)
        last = 0
        for i in range(len(intervals)):
            if intervals[i].start < last:
                return False
            last = intervals.end
        return True


if __name__ == "__main__":
    intervals = [(0, 30), (5, 10), (15, 20)]
    intervals = [Interval(a[0], a[1]) for a in intervals]
    ans = False
    resp = Solution().canAttendMeetings(intervals)

    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)
