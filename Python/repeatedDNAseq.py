class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        """
        O(n) time
        O(n) space
        """
        check = set()
        duplicate = set()
        for i in range(len(s) - 9):
            tmp = s[i:i + 10]
            if tmp in check:
                duplicate.add(tmp)
            else:
                check.add(tmp)
        return list(duplicate)




