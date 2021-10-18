import collections

from utils import TreeNode, build_tree, tree_to_list


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        BFS encode
        O(n) time


        :type root: TreeNode
        :rtype: str
        """
        from collections import deque
        res = []

        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    res.append(str(node.val))
                    q.append(node.left)
                    q.append(node.right)
                else:
                    res.append("None")
        while len(res) > 0 and res[-1] == "None":
            res.pop()
        return ".".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        BFS decode
        O(n) time

        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None
        buff = data.split(".")
        buff = [eval(a) for a in buff]
        data = collections.deque(buff)
        head = TreeNode(data.popleft())
        lvl = collections.deque([head])
        while data:

            for i in range(len(lvl)):
                node = lvl.popleft()
                if node and node.val is not None:
                    if data:
                        left = data.popleft()
                        lnode = TreeNode(left)
                        lvl.append(lnode)
                        if left is not None:
                            node.left = lnode
                    if data:
                        right = data.popleft()
                        rnode = TreeNode(right)
                        lvl.append(rnode)
                        if right is not None:
                            node.right = rnode

        return head


if __name__ == "__main__":
    null = None
    tmp = [4, -7, -3, null, null, -9, -3, 9, -7, -4, null, 6, null, -6, -6, null, null, 0, 6, 5, null, 9, null, null,
           -1, -4, null, null, null, -2]
    root = build_tree(tmp)

    ans = tmp
    resp = Codec().serialize(root)
    print(tree_to_list(Codec().deserialize(resp)))

    # print(tree_to_list(resp))
    # print(tree_to_list(resp))
    # if ans == resp:
    #     print("PASS", resp, "-" * 10)
    # else:
    #     print("FAIL", resp, "-" * 10)
