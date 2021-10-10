class Solution:
    def eraseOverlapIntervals(self, intervals:list) -> int:
        """
        O(nlogn) time
        O(n) space

        :param intervals:
        :return:
        """
        intervals.sort(key = (lambda x: x[1]))
        last = -1e5
        count = 0
        for inter in intervals:
            if inter[0] < last:
                count += 1
            else:
                last = inter[1]
        return count



if __name__ == "__main__":
    intervals = [[1,2],[2,3],[3,4],[-100,-2],[5,7]]
    ans =  0
    resp = Solution().eraseOverlapIntervals(intervals)

    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)
