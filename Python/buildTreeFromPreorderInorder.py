import collections

from utils import TreeNode, build_tree, tree_to_list


class Solution:
    def buildTree(self, preorder: list, inorder: list) -> TreeNode:
        """
        DFS,
        O(n) time and space

        :param preorder:
        :param inorder:
        :return:
        """
        if len(inorder) == 1:
            head_val = preorder.pop(0)
            return TreeNode(inorder[0])
        if len(inorder) == 0:
            return
        head_val = preorder.pop(0)
        head_val_idx = inorder.index(head_val)

        head = TreeNode(head_val)

        left_inorder = inorder[:head_val_idx]
        right_inorder = inorder[head_val_idx + 1:]
        head.left = self.buildTree(preorder, left_inorder)
        head.right = self.buildTree(preorder, right_inorder)
        return head


if __name__ == "__main__":
    preorder = [1,2,3]
    inorder = [1,2,3]

    ans = True
    resp = Solution().buildTree(preorder, inorder)
    print(tree_to_list(resp))
    if ans == resp:
        print("PASS", resp, "-" * 10)
    else:
        print("FAIL", resp, "-" * 10)
