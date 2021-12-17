class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        """O(n) time"""

        v1 = version1.split(".")
        v2 = version2.split(".")
        for i in range(max(len(v1), len(v2))):
            a = v1[i] if i < len(v1) else 0
            b = v2[i] if i < len(v2) else 0
            if int(a) > int(b):
                return 1
            elif int(a) < int(b):
                return -1
        return 0


