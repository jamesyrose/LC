from utils import TreeNode, build_tree

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """
        DFS
        O(N) where N is number of edges
        O(N) space
        :param root:
        :return:
        """
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))



    def maxDepth2(self, root: TreeNode) -> int:
        """
        BFS
        O(N) where N is number of edges
        O(N) space

        :param root:
        :return:
        """
        from collections import deque
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 0

        depth = 0
        queue = deque([root])
        while len(queue) > 0:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.right is not None:
                    queue.append(node.right)
                if node.left is not None:
                    queue.append(node.left)
            depth += 1
        return depth





if __name__ == "__main__":
    root = [3,9,20,None,None,15,7]
    root = build_tree(root)
    ans = 3
    resp = Solution().maxDepth2(root)
    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)