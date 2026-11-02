def is_palindrome(s: str, left: int, right: int) -> bool:
    while left < right:

        if s[left] != s[right]:
            return False

        left += 1
        right -= 1

    return True
    
class Solution:

    def validPalindrome(self, s: str) -> bool:

        left, right = 0, len(s) - 1
        left_pal, right_pal = False, False

        while left < right:
            if s[left] != s[right]:

                if s[left + 1] == s[right]:
                    left_pal = is_palindrome(s, left + 1, right)
                if s[right - 1] == s[left]:
                    right_pal = is_palindrome(s, left, right - 1)
                return left_pal or right_pal

            left += 1
            right -= 1

        return True
                

    # abbab