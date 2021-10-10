# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def create_node_input(input: list) -> 'Node':
    temp_dict = {}
    for i in range(1, len(input) + 1):
        temp_dict[i] = Node(val=i)

    for i in temp_dict.keys():
        neighbors = [temp_dict[a] for a in input[i - 1]]
        temp_dict[i].neighbors = neighbors

    return temp_dict[1]




class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        """
        O(n) time
        O(n) space
        :param node:
        :return:
        """
        # key is val, value is neighbors
        if not node:
            return None
        old_to_new = {}

        def dfs(node: 'Node'):
            if node in old_to_new:
                return old_to_new[node]
            old_to_new[node] = Node(node.val)
            for n in node.neighbors:
                old_to_new[node].neighbors.append(dfs(n))
            return old_to_new[node]
        return dfs(node)





if __name__ == "__main__":
    adjList = [[2,4],[1,3],[2,4],[1,3]]
    out = [[2,4],[1,3],[2,4],[1,3]]
    ans = False
    adjList = create_node_input(adjList)
    print(adjList)
    resp = Solution().cloneGraph(adjList)
    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)

