from utils import TreeNode, build_tree, tree_to_list

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        """
        DFS
        O(n) time


        :param root:
        :return:
        """

        def dfs(node):
            if node == None or node.val == None:
                return 0
            l, r = dfs(node.left), dfs(node.right)
            local_max = max( node.val + l, node.val + r, node.val)
            dfs.global_max = max(dfs.global_max, local_max, node.val + l + r)
            print(node.val, l, r, dfs.global_max)
            return local_max
        if root == None:
            return 0
        dfs.global_max = root.val
        dfs(root)
        return dfs.global_max





if __name__ == "__main__":
    test_cases = [
        [[5,4,8,11,None,13,4,7,2,None,None,None,None,1], 48],
        [[-10,9,20,None, None,15,7], 42],
        [[1,2,3], 6]
    ]
    for c in test_cases:
        root = build_tree(c[0])

        ans = c[1]
        resp = Solution().maxPathSum(root)
        # print(tree_to_list(resp))
        if ans == resp:
            print("PASS", resp, "-" * 10)
        else:
            print("FAIL", resp, "-" * 10)
