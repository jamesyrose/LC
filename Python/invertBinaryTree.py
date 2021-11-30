from utils import TreeNode, build_tree, tree_to_list

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        """
        DFS solution
        O(n) time
        O(n) space

        :param root:
        :return:
        """
        if not root:
            return root
        buff = root.right
        root.right = root.left
        root.left = buff
        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)
        return root




if __name__ == "__main__":
    root = build_tree([4,2,7,1,3,6,9])

    ans = 3
    resp = Solution().invertTree(root)
    print(tree_to_list(resp))
    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)
