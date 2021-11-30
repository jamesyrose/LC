class Solution:
    def maxArea(self, height: list) -> int:
        l, r = 0, len(height) - 1
        max_area = 0
        for i in range(len(height)):
            area = (r - l) * min(height[l], height[r])
            if area > max_area:
                max_area = area
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return max_area





if __name__ == "__main__":
    height = [2,3,4,5,18,17,6]
    ans = 17
    resp = Solution().maxArea(height)
    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)