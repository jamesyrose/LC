class Solution:
    def canFinish(self, numCourses: int, prerequisites: list) -> bool:
        """
        O(n + m) time

        :param numCourses:
        :param prerequisites:
        :return:
        """
        map = {i: [] for i in range(numCourses)}
        visited = set()
        for req in prerequisites:
            map[req[0]].append(req[1])

        def dfs(course):
            if course in visited:
                return False
            if not map[course]:
                return True

            visited.add(course)
            for req in map[course]:
                if not dfs(req): return False
            visited.remove(course)
            map[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course): return False
        return True


if __name__ == "__main__":
    numCourses = 2
    prerequisites = [[1, 0]]
    ans = False
    resp = Solution().canFinish(numCourses, prerequisites)
    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)
