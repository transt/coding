# Problem: Reverse a String In-Place
# 
# Write a function that reverses a list of characters in-place.
# 
# You must do this by modifying the input list in-place with O(1) extra memory — do not return a new string or list.
# Example:
# 
#     Input:  ["h", "e", "l", "l", "o"]
#     Output: ["o", "l", "l", "e", "h"]
# 
#     Constraints:
# 
#         The input is a list of characters s (not a string).
#         You must modify the input list directly.
#         Do not use built-in functions like reverse() or slicing.


from typing import List


class Solution:

    def reverse_string_inplace(self, s: List) -> List:
        s_len = len(s)
        l = 0
        r = s_len - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1


sol = Solution()
test_string = list("hello")
sol.reverse_string_inplace(test_string)
print(f"{list('hello')} => {test_string}")
