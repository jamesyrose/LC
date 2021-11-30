from utils import TreeNode, build_tree, tree_to_list

class Solution:
    def levelOrder(self, root: TreeNode) -> list:
        """
        bfs
        O(n) time
        O(n) space

        :param root:
        :return:
        """
        from collections import deque
        res = []

        q = deque([root])
        while q:
            lvl = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    if node.val is not None:
                        lvl.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            res.append(lvl)
        return res[:-1]







if __name__ == "__main__":
    test_cases = [
        [[3,9,20,None, None,15,7], [[3],[9,20],[15,7]]],
        [[0,2,4,1,None,3,-1,5,1,None,6,None,8],[[0],[2,4],[1,3,-1],[5,1,6,8]]]
    ]
    for c in test_cases:
        root = build_tree(c[0])

        ans = c[1]
        resp = Solution().levelOrder(root)
        # print(tree_to_list(resp))
        if ans == resp:
            print("PASS", resp, "-" * 10)
        else:
            print("FAIL", resp, "-" * 10)
