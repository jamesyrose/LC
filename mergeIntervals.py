class Solution:
    def merge(self, intervals:list) -> list:
        """
        O(n log n) time
        O(n) space

        :param intervals:
        :param newInterval:
        :return:
        """
        # sort intervals by first index
        intervals = sorted(intervals) # O(n log n) time O(n) space

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
    intervals = [[1, 3],  [8, 10], [2, 6], [15, 18]]
    ans =  [[1,6],[8,10],[15,18]]
    resp = Solution().merge(intervals)

    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)
