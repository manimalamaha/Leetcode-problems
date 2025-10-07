class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)[::-1]
        if s== str(x):
            return True
        else:
            return False