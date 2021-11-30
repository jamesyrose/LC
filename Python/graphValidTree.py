class Solution:
    def validTree(self, n, edges):
        """
        DFS
        O(n) where n = Edges + nodes
        :param n:
        :param edges:
        :return:
        """
        neigh = {i: [] for i in range(n)}
        for edge in edges:
            neigh[edge[0]].append(edge[1])
            neigh[edge[1]].append(edge[0])

        visit = set()

        def dfs(node, last):
            if node in visit:
                return False
            visit.add(node)
            for i in neigh[node]:
                if i != last:
                    if not dfs(i, node):
                        return False
            return True

        return dfs(0, -1) and len(visit) == n