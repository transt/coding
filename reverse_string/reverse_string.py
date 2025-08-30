# Problem: Reverse a String
#
# Write a function that takes a string as input and returns the string reversed.
# Example:
#     Input: "hello"
#     Output: "olleh"
# 

class Solution:
    def reverse_string(self, s: str) -> str:
        return s[::-1]


if __name__ == "__main__":
    sol = Solution()
    tests = [
        (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
        (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"])
    ]

    for i, (arg, expected) in enumerate(tests, 1):
        result = sol.reverse_string(arg)
        print(f"Test {i}: reverse_string({arg}) => result={result}, expected={expected}")
        assert result == expected, f"Test {i} failed! Expected={expected}, got={result}"
    print("All tests passed!")
