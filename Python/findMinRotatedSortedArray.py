class Solution:
    def findMin(self, nums: list) -> int:
        """
        O(log n) because halfs every recursion (binary search)

        :param nums:
        :return:
        """

        def find_min_sub(nums1, nums2):
            # compare tail ends, they will contain max of sub array containing min vals,
            # so the one with lower val should be searched
            # i.e.  [4,5,6,7] and [8,9,0,1,2]  the 2 being less than 7 means that the second array
            # will contain the lower tail of th entire array
            if nums1[-1] > nums2[-1]:
                if len(nums2) <= 2:
                    return min(nums2)
                midpnt = len(nums2) // 2
                return find_min_sub(nums2[:midpnt], nums2[midpnt:])
            else:
                if len(nums1) <= 2:
                    return min(nums1)
                midpnt = len(nums1) // 2
                return find_min_sub(nums1[:midpnt], nums1[midpnt:])

        # Base case, only 2 elements to compare
        if len(nums) <= 2:
            return min(nums)
        # recursion
        mid_pnt = len(nums) // 2
        return find_min_sub(nums[:mid_pnt], nums[mid_pnt:])


if __name__ == "__main__":
    nums = [1, 2, 3]
    ans = 1
    resp = Solution().findMin(nums)
    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)
