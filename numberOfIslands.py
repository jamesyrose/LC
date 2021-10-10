class Solution:
    def numIslands(self, grid: list) -> int:
        """
        O(n^2) time
        O(1) space

        :param grid:
        :return:
        """
        islands = 0
        R, C  = len(grid), len(grid[0])
        def dfs(r, c):
            if r == R or c == C or r < 0 or c < 0 or grid[r][c] != "1":
                return False # return False if point is part of island or ocean (0)
            grid[r][c] = "0" # modify grid indicates checked points
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            return True
        for r in range(R): # O(n^2) nested for loop, will only check every point once
            for c in range(C):
                if dfs(r, c):
                    islands += 1
        return islands









if __name__ == "__main__":
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    ans = 3
    resp = Solution().numIslands(grid)

    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)
