from utils import TreeNode, build_tree


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if (p and not q) or (q and not p):
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)




    def isSameTreeBFS(self, p: TreeNode, q: TreeNode) -> bool:
        """
        BFS with two queues
        O(n) time where n is the number of edges

        :param p:
        :param q:
        :return:
        """
        from collections import deque
        if p is None and q is None:
            return True
        elif (p is None and q is not None) or (p is not None and q is None):
            return False

        pq = deque([p])
        qq = deque([q])

        while len(pq) > 0 and len(qq) > 0:
            if len(pq) != len(qq):
                # If there not the same length they dont have the same number of nodes
                return False
            for i in range(len(pq)):
                tmpp, tmpq = pq.popleft(), qq.popleft()
                if tmpp and tmpq:
                    if tmpp.val != tmpq.val:
                        return False
                    else:
                        pq.append(tmpp.left)
                        qq.append(tmpq.left)
                        pq.append(tmpp.right)
                        qq.append(tmpq.right)
                elif (tmpp and not tmpq) or (tmpq and not tmpp):
                    return False
        return True


if __name__ == "__main__":
    p = build_tree([1, 2, 1])
    q = build_tree([1,  1,2])

    ans = 3
    resp = Solution().isSameTree(p, q)
    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)
