class Solution:
    def setZeroes(self, matrix: list) -> None:
        """
        O(n^2) time
        O(n + m ) space
        """
        c0 = set() # O(n) space (worst case)
        r0 = set() # O(m) space (worst case)

        R, C = len(matrix), len(matrix[0])
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:
                    c0.add(j)
                    r0.add(i)
        for i in r0:
            matrix[i] = [0] * C
        for j in c0:
            for i in range(R):
                matrix[i][j] = 0
        return matrix

    def setZeroes2(self, matrix: list) -> None:
        """
        O(n^2) time
        O(1) space
        """
        R, C = len(matrix), len(matrix[0])

        if any([a==0 for a in matrix[0]]):
            firstRow = True
        else:
            firstRow = False
        for i in range(1, R):
            for j in range(C):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(1, R):
            if matrix[i][0] == 0:
                matrix[i] = [0] * C
        for j in range(C):
            if matrix[0][j] == 0:
                for i in range(1, R):
                    matrix[i][j] = 0
        if firstRow:
            matrix[0] = [0] * C

        return matrix




if __name__ == "__main__":
    matrix = [[-4,-2147483648,6,-7,0],[-8,6,-8,-6,0],[2147483647,2,-9,-6,-10]]
    ans = [[0,0,0,0,0],[0,0,0,0,0],[2147483647,2,-9,-6,0]]
    resp = Solution().setZeroes2(matrix)
    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)