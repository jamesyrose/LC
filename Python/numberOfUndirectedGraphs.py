"""
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""

class Solution:
    def connectedSet(self, nodes):
        """
        O(n log n) for the sorting at the end.
        O(n) for dfs where n = Edges +  Nodes
        :param nodes:
        :return:
        """
        visit = set()
        sub = set()
        res = []

        def dfs(node):
            if node in visit:
                return
            visit.add(node)
            sub.add(node)
            for n in node.neighbors:
                dfs(n)
            return


        for n in nodes:
            sub = set()
            dfs(n)
            if len(sub) > 0:
                res.append(sorted([s.label for s in sub]))
        return sorted(res)