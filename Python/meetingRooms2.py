class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals: list) -> int:
        """
        O(n log n) time
        O(n) space

        :param intervals:
        :return:
        """
        start, end = [], []
        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)
        start = sorted(start)
        end = sorted(end)
        count = 0
        sp, ep = 0, 0
        max_count = 0
        while  sp < len(start) and ep < len(end):
            if end[ep] >= start[sp]:
                count += 1
                sp += 1
            else:
                count -= 1
                ep = 1
            max_count = max(count, max_count)

        return max_count



if __name__ == "__main__":
    intervals = [(0,30),(5,10),(15,20)]
    intervals = [Interval(a[0], a[1]) for a in intervals]
    ans = 2
    resp = Solution().minMeetingRooms(intervals)
    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)
