class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        copy = str(x)
        copy = copy[::-1]
        if (copy == str(x)):
            return True
        return False
