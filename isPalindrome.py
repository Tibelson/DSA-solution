class Solution:
    def isPalindrome(self, x: int) -> bool:
        new = str(x)
        reverse = new[::-1]
        if reverse == new:
            return True
        return False