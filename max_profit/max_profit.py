from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
        ([0], 0)
    ]

    for i, (arg, expected) in enumerate(tests, 1):
        result = sol.maxProfit(arg)
        print(f"Test {i}: maxProfit({arg}) => result={result}, expected={expected}")
        assert result == expected, f"Test {i}: failed! Expected={expected}, got={result}"

    print("All tests passed!")
