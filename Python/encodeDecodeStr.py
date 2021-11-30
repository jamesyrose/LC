class Solution:
    """
    Literally adding a delimiter

    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        """
        O(n) for join
        :param strs:
        :return:
        """
        return "<?>>:{}+_+".join(strs)

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        """
        O(n) for split
        :param str:
        :return:
        """
        # write your code here
        return str.split("<?>>:{}+_+")