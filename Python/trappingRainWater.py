class Solution:
    def trap(self, height: List[int]) -> int:
        """
        O(n) time
        O(1) space
        """
        total_sum = 0
        # Left to right

        maxIdx = height.index(max(height))
        l, r = 0, len(height) - 1
        lmax, rmax = height[l], height[r]

        l += 1
        r -= 1
        while l < maxIdx or r > maxIdx:
            if l < maxIdx:
                if height[l] < lmax:
                    total_sum += lmax - height[l]
                else:
                    lmax = height[l]
                l += 1
            if r > maxIdx:
                if height[r] < rmax:
                    total_sum += rmax - height[r]
                else:
                    rmax = height[r]
                r -= 1
        return total_sum
