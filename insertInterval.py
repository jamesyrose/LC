class Solution:
    def insert(self, intervals: list, newInterval: list) -> list:
        """
        O(n) time
        O(n) space

        :param intervals:
        :param newInterval:
        :return:
        """
        # base case (empty)
        if len(intervals) == 0:
            return [newInterval]

        # insert it
        if newInterval[0] <= intervals[0][0]:
            intervals = [newInterval] + intervals
        elif newInterval[0] >= intervals[-1][0]:
            intervals += [newInterval]
        else:
            i = 0
            while i < len(intervals) - 1:
                if intervals[i][0] <= newInterval[0] <= intervals[i + 1][0]:
                    intervals = intervals[:i+1] + [newInterval] + intervals[i+1:]
                    break
                i += 1
        # join
        i = 1
        while  i < len(intervals):
            prior = intervals[i - 1]
            curr = intervals[i]
            if curr[0] <= prior[1]:
                intervals[i - 1] = [prior[0], max(curr[1], prior[1])]
                intervals.pop(i)
            else:
                i += 1
        return intervals


if __name__ == "__main__":
    intervals =[[1,5]]
    newInterval = [0,10]
    ans =  [[1,2],[3,10],[12,16]]
    resp = Solution().insert(intervals, newInterval)

    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)
