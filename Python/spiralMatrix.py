class Solution:
    def spiralOrder(self, matrix: list) -> list:
        """
        O(n * m) time
        O(n * m) space

        :param matrix:
        :return:
        """
        def popCol(matrix, num):
            col = []
            for i in range(len(matrix)):
                col.append(matrix[i][num])
                matrix[i].pop(num)
            return matrix, col

        res = [] # O(n * m)
        reverse = False
        while len(matrix) > 0 and len(matrix[0]) > 0:
            if reverse:
                # take row
                matrix[-1].reverse()
                res += matrix[-1]
                matrix = matrix[:-1]
                # take col
                matrix, col = popCol(matrix, 0)
                col.reverse()
                res += col
                reverse = False
            else:
                # take row
                res+= matrix[0]
                matrix = matrix[1:]
                # take col
                matrix, col = popCol(matrix, -1)
                res+= col
                reverse =True

        return res








if __name__ == "__main__":
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    ans = [1,2,3,4,8,12,11,10,9,5,6,7]
    resp = Solution().spiralOrder(matrix)
    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)