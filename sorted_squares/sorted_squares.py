"""
Given an integer array nums sorted in non-decreasing order, return
an array of the squares of each number sorted in non-decreasing order.
"""

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        result = []
        while left <= right:
            if abs(nums[left]) < abs(nums[right]):
                result.append(nums[right] ** 2)
                right -= 1
            else:
                result.append(nums[left] ** 2)
                left += 1
        result.reverse()
        return result


if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([-4, -2, 0, 1, 4, 10], [0, 1, 4, 16, 16, 100]),
        ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121]),
        ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100])
    ]

    for i, (arg, expected) in enumerate(tests, 1):
        result = sol.sortedSquares(arg)
        print(f"Test {i}: sortedSquares({arg}) => result={result}, expected={expected}")
        assert result == expected, f"Test {i}: failed! Expected={expected}, got={result}"

    print("All tests passed!")
