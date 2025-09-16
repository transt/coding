from typing import Dict


class Solution:
    def fib_recursive(self, n: int) -> int:
        # Time: O(2 ** n)
        # Space: O(n)
        if n == 0:
            return 0
        if n == 1:
            return 1

        return self.fib_recursive(n - 2) + self.fib_recursive(n - 1)

    def fib_dynamic_topdown(self, n: int) -> int:
        # Time: O(n)
        # Space: O(n)
        memo = {0: 0, 1: 1}

        def fib(x: int) -> int:
            if x in memo:
                return memo[x]

            memo[x] = fib(x - 1) + fib(x - 2)
            return memo[x]

        return fib(n)

    def fib_dynamic_bottomup(self, n: int) -> int:
        # Time: O(n)
        # Space: O(n)

        if n == 0:
            return 0
        if n == 1:
            return 1

        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 2] + dp[i - 1]

        return dp[n]


if __name__ == "__main__":
    sol = Solution()
    tests = [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13)
    ]

    for i, (arg, expected) in enumerate(tests, 1):
        result = sol.fib_dynamic_topdown(arg)
        print(f"Test {i}, sol.fib_dynamic_topdown({arg}) => result={result}, expected={expected}")
        assert result == expected, "Test {i} failed! Expected={expected}, Got={result}"
    print("All tests passed!") 
