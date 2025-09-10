class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True

        n = len(s)
        left = 0
        right = n - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        ("", True)
    ]

    for idx, (arg, expected) in enumerate(tests, 1):
        result = sol.isPalindrome(arg)
        print(f"Test {idx}: isPalindrome(\"{arg}\") => result={result}, expected={expected}")
        assert result == expected, f"Test {idx} failed! Expected={expected}, got={result}"

    print("All tests passed!")
