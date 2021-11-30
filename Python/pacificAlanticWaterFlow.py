class Solution:
    def pacificAtlantic(self, heights: list) ->list:
        # tuple (pacific, atlantic)
        R, C  = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r, c, ocean, last):
            if  (r,c) in ocean or r == R or c == C or r < 0 or c <0 or heights[r][c] < last :
                return

            ocean.add((r,c))
            dfs(r + 1, c, ocean, heights[r][c])
            dfs(r - 1, c, ocean, heights[r][c])
            dfs(r, c + 1, ocean, heights[r][c])
            dfs(r, c -1, ocean, heights[r][c])

        for c in range(C):
            dfs(0, c, pacific, heights[0][c])
            dfs(R - 1, c, atlantic, heights[R-1][c])


        for r in range(R):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, C - 1, atlantic, heights[r][C -1])

        res = []
        for point in pacific:
            if point in atlantic:
                res.append(list(point))
        return res

            


if __name__ == "__main__":
    heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
    ans = [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
    resp = Solution().pacificAtlantic(heights)

    if all([a in ans for a in resp]) and len(ans) == len(resp):
        print("PASS", resp)
    else:
        print("FAIL", resp)
