import collections

from utils import TreeNode, build_tree, tree_to_list


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        O(log n)  time because it is only going to check one side of the tree at a time
        O(1) space
        :param root:
        :param p:
        :param q:
        :return:
        """
        while root:
            if p.val > root.val and q.val > root.val:
                root = root.right
            elif p.val < root.val and q.val < root.val:
                root = root.left
            else:
                return root


    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        DFS
        O(log n) time and space because it will only go down one side of the tree
        (assuming tree random/ somewhat symmetrical)

        :param root:
        :param p:
        :param q:
        :return:
        """

        # if p or q == node then that is the ancestor
        if p.val == root.val or q.val == root.val:
            return root
        # search right if p and q are greater
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        # search left if p and q are less
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        # return root,  if p and q are in different subtrees  (LCA)
        return root





if __name__ == "__main__":
    null = None
    test_case = [
        [[6,2,8,0,4,7,9,null,null,3,5], 2, 8],
        [[6,2,8,0,4,7,9,null,null,3,5], 2, 4],
        [[3,1,4,null,2], 2, 3]
    ]
    for test in test_case:
        root = build_tree(test[0])
        ans = False
        resp = Solution().lowestCommonAncestor(root, TreeNode(test[1]), TreeNode(test[2]))
        print(resp.val)
        if ans == resp:
            print("PASS", resp, "-" * 10)
        else:
            print("FAIL", resp, "-" * 10)
