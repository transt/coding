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


sol = Solution()
print(f"'hello' => {sol.reverse_string('hello')}")
