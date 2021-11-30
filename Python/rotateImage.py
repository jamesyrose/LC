class Solution:
    def rotate(self, matrix: list) -> list:
        """
        O(n^2) time
        O(1) space
        :param matrix:
        :return:
        """
        R, C = len(matrix), len(matrix[0])
        L, R, T, B = 0, C - 1, 0, R - 1
        while R > L:
            for i in range(R - L):
                buff = matrix[T][L + i]
                matrix[T][L+ i] = matrix[B - i][L]
                matrix[B-i][L] = matrix[B][R -i]
                matrix[B][R - i] = matrix[T+i][R]
                matrix[T+i][R] = buff
            T += 1
            L += 1
            R -= 1
            B -= 1

        return matrix



if __name__ == "__main__":
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    ans = [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
    resp = Solution().rotate(matrix)
    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)
