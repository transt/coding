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

    def reverse_string_inplace(self, s: List[str]) -> None:
        n = len(s)
        l = 0
        r = n - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

if __name__ == "__main__":
    sol = Solution()
    tests = [
        (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
        (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"])
    ]

    for i, (arg, expected) in enumerate(tests, 1):
        sol.reverse_string_inplace(arg)
        result = arg
        print(f"Test {i}: reverse_string_inplace({arg}) => result={result}, expected={expected}")
        assert result == expected, f"Test {i} failed! Expected={expected}, got={result}"
    print("All tests passed!")
