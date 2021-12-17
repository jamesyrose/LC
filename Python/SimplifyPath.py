class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        O(n) time
        O(n) space
        """

        # remove tail /
        path = path.rstrip("/")

        # join paths
        res = []
        for p in path.split("/")[1:]:
            if p == "..":
                if len(res) > 0:
                    res.pop()
            elif p == "." or p == "":
                pass
            else:
                res.append(p)
        return "/" + "/".join(res)


