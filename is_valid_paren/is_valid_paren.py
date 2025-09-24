"""
Given a string s containing just the character '(', ')', '{', '}', '[', and ']',
determine if the input string is valid.

An input string is valid if:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.
    3. Every close bracket has a corresponding open bracket of the same type.
"""


class Solution:
    def isValidParen(self, s: str) -> bool:
        paren = {
            "]": "[",
            ")": "(",
            "}": "{"
        }
        paren_stack = []
        for c in s:
            if c in paren.values():
                paren_stack.append(c)
            elif c in paren:
                if not paren_stack or paren_stack.pop() != paren[c]:
                    return False
            else:
                return False
        return not paren_stack



if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("()", True),
        ("()[]{}", True),
        ("(}", False),
        ("asdf", False),
        ("", True),
        ("{([])}", True)

    ]

    for i, (args, expected) in enumerate(tests, 1):
        result = sol.isValidParen(args)
        print(f"Test {i}, running isValidParen({args}) => result={result}, expected={expected}")
        assert result == expected, f"Test {i} Failed! Expected={expected}, Got={result}"
    print("All tests passed!")
