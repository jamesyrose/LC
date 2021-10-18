from utils import TreeNode, build_tree, tree_to_list


class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        """
        O(r * s) time and space, where r is size of root and s is size of subroot

        :param root:
        :param subRoot:
        :return:
        """
        if not subRoot:
            return True
        if not root:
            return False
        if self.sameTree(root, subRoot):
            return True
        self.isSubtree(root.right, subRoot)
        self.isSubtree(root.left, subRoot)


    def sameTree(self, root, sub):
        if not root and not sub:
            return True
        if  root and sub and root.val == sub.val:
            return (self.sameTree(root.right, sub.right) and self.sameTree(root.left, sub.left))
        return False




if __name__ == "__main__":
    root = build_tree([1,1])
    subRoot = build_tree([1])

    ans = True
    resp = Solution().isSubtree(root, subRoot)
    # print(tree_to_list(resp))
    if ans == resp:
        print("PASS", resp, "-" * 10)
    else:
        print("FAIL", resp, "-" * 10)
