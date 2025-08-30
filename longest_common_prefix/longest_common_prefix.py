from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = float('inf')
        i = 0
        for s in strs:
            min_length = min(min_length, len(s))

        while i < min_length:
            for s in strs:
                if s[i] != strs[0][i]:
                    return s[:i]
            i += 1
        return strs[0]


if __name__ == "__main__":
    sol = Solution()
    tests = [
        (["flowers", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
    ]

    for i, (arg, expected) in enumerate(tests, 1):
        result = sol.longestCommonPrefix(arg)
        print(f"Test {i}: longestCommonPrefix({arg}) => result={result}, expected={expected}")
        assert result == expected, f"Test {i}: failed: exected {expected}, got {result}"

    print("All tests passed!")
