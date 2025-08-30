"""
Given a 1-indexed array of integers num that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number.
"""

from typing import List


class Solution:
    def twoSum2(self, num: List[int], target: int) -> List[int]:
        n = len(num)
        l = 0
        r = n - 1
        while l < r:
            summ = num[l] + num[r]
            if summ == target:
                return [l + 1, r + 1]

            if summ < target:
                l += 1
            else:
                r -= 1


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([2, 7, 11, 15], 9, [1, 2]),
        ([1, 5, 10, 11, 15, 25], 21, [3, 4]),
        ([2, 3, 4], 6, [1, 3])
    ]

    for i, (num, target, expected) in enumerate(tests, 1):
        result = sol.twoSum2(num, target)
        print(f"Test {i}: twoSum2({num}, {target}) => result={result}, expected={expected}")
        assert result == expected, f"Test {i}: failed! Expected={expected}, got={result}"

    print("All tests passed!")
