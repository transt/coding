class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == '':
            return True
        if len(s) > len(t):
            return False
        for i in s:
            if i not in t:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()

    tests = [
        ("abc", "ahbgdc", True),
        ("axc", "ahbgdc", False),
        ("acf", "abcdef", True),
        ("acf", "abcdeg", False)
    ]

    for i, (s, t, expected) in enumerate(tests, 1):
        result = sol.isSubsequence(s, t)
        print(f"Test {i}: sol.isSubsequence({s}, {t})  => {result} (expected: {expected})")
        assert result == expected, f"Test {i}: failed: expected {expected}, got {result}"

    print("Al tests passed!")
